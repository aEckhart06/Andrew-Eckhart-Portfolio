
const FIREBASE_PROJECT_ID = 'PROJECT_ID';
const FIREBASE_API_KEY = 'PRIVATE_API_KEY';

function getMainFirestoreUrl(collectionPath, documentId) {
  return `https://firestore.googleapis.com/v1/projects/${FIREBASE_PROJECT_ID}/databases/(default)/documents/${collectionPath}/${documentId}key=${FIREBASE_API_KEY}`;
}

function getFirestoreUrl(collectionPath, documentId) {
  const baseUrl = `https://firestore.googleapis.com/v1/projects/${FIREBASE_PROJECT_ID}/databases/(default)/documents`;
  return documentId 
  ? `${baseUrl}/${collectionPath}/${documentId}?key=${FIREBASE_API_KEY}` 
  : `${baseUrl}/${collectionPath}?key=${FIREBASE_API_KEY}`;
}

function replaceCurlyApostrophes(inputString) {
  // Replace curly apostrophe (’) with straight apostrophe (')
  return inputString.split("’").join("'");
}

function encodeApostrophes(inputString) {
  return inputString.split("'").join("%27");
}

function encodeForURL(inputString) {
  // Replace curly apostrophes and then encode the string
  const cleanedString = replaceCurlyApostrophes(inputString);
  const partiallyEncodedString = encodeURIComponent(cleanedString);
  return encodeApostrophes(partiallyEncodedString);
}


function createSubcollection(documentId, lastRowWithData, currentColumnData, sheet) {

  const timestampIndex = 1;
  const userEmailIndex = 2;
  const userFirstNameIndex = 3;
  const userLastNameIndex = 4;

  const collectionName = 'momAnswersCollection';
  const subcollectionName = 'answersCollection'; // The name of the subcollection to be created

  if (documentId.includes("?")) {
    let f = documentId.indexOf("?");
    documentId = documentId.substr(0, f);
  }

  
  for (let i = 1; i < lastRowWithData; i++) { //---------------------------------------------------------------

    var subDocId = currentColumnData[i];
    var subDocId = subDocId.toString();
    //subDocId = encodeForURL(subDocId);

    Logger.log("DATA: " + documentId + subDocId + " " + lastRowWithData);

    const subcollectionUrl = getFirestoreUrl(`${collectionName}/${documentId}/${subcollectionName}`, subDocId);
    Logger.log("SUBURL: " + subcollectionUrl);


    var cellData = currentColumnData[i];
    if (cellData) { // Only create documents for non-empty cells
      // Create the placeholder document in the subcollection
      const subcollectionData = {
        fields: {
            answer: { stringValue: cellData.toString() },
            timeStamp: { stringValue: sheet.getRange(i+1, timestampIndex).getValues().toString()},
            userEmail: { stringValue: sheet.getRange(i+1, userEmailIndex).getValues().toString()},
            firstName: { stringValue: sheet.getRange(i+1, userFirstNameIndex).getValues().toString()},
            lastName: { stringValue: sheet.getRange(i+1, userLastNameIndex).getValues().toString()}
          }
      };
      const options = {
        method: 'PATCH',
        contentType: 'application/json',
        payload: JSON.stringify(subcollectionData),
        muteHttpExceptions: true
      };

      try {
        const response = UrlFetchApp.fetch(subcollectionUrl, options);

        // Log the full response, even if there was an error (e.g., 400 or 500)
        Logger.log("HTTP Status Code: " + response.getResponseCode());
        Logger.log("Response Body: " + response.getContentText());

        if (response.getResponseCode() >= 200 && response.getResponseCode() < 300) {
          Logger.log("Document added/updated with ID: " + documentId);
        } else {
          Logger.log("Error adding/updating document. Status Code: " + response.getResponseCode());
        }
      } catch (error) {
        Logger.log(`Error: ${error}`);
      }
      
    }
  }

  
  
}


function testOnEdit() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const e = {
    source: SpreadsheetApp.getActiveSpreadsheet(),
    range: sheet.getRange("G1") // Adjust as needed for testing
  };
  onEdit(e);
}


function onEdit(e) {
  const startIndex = 7; // Set this to the index where you want to start reading (e.g., 2 for column B)

  const collectionName = 'momAnswersCollection';

  // Check if the event object exists (which it should when triggered by an edit)
  if (!e) {
    Logger.log("No event object passed. Ensure this function is triggered by an edit in the sheet.");
    return; // Exit if there's no event object
  }

  const sheet = e.source.getActiveSheet();
  const sheetName = sheet.getName();
  const range = e.range;
  const row = range.getRow();
  const numRows = sheet.getLastRow();
  const numColumns = sheet.getLastColumn();

  // Only proceed if the row number is valid and greater than or equal to 1 (first row)
  if (row >= 1) {

    const rowData = sheet.getRange(row, startIndex, numRows, numColumns - startIndex + 1).
      getValues()[0]; //getRange(row, column, numRows, numColumns)

    // For each column in the dataset
    for (let j = 1; j < rowData.length; j++) { //---------------------------------------------------------------------
      
      // Get the last row that contains data in the current column
      // The question is always index 0
      const currentColumnData = sheet.getRange(1, startIndex - 1 + j, sheet.getLastRow()).getValues();
      var lastRowWithData = 0;
      for (var f = currentColumnData.length - 1; f >= 0; f--) {
        if (currentColumnData[f][0] !== "") {
          Logger.log("The last row with data in the current column is: " + (f + 1));
          lastRowWithData = f + 1; // Return the last row with data
          break;
        }
      }

      var questionCellData = currentColumnData[0];

      // Remove the "Hey Mom," at the beginning of each question.
      questionCellData = questionCellData.toString();

      if (questionCellData.includes("Hey Mom, ")) {
        questionCellData = questionCellData.substr(9, questionCellData.length);
        questionCellData = questionCellData.charAt(0).toUpperCase() + questionCellData.slice(1);
      } 
      
      // Filter out any "(Male)" or "(Female)"
      if (questionCellData.includes("(")) {
        let f = questionCellData.indexOf("(")
        questionCellData = questionCellData.substr(0, f-1);
      }

      const docData = {
        fields: {
          question: { stringValue: questionCellData },
          /* catagoryId */ sheetId: { stringValue: sheetName.toString()} 
        }
      };


      const docId = questionCellData; // Use the cell data as the document ID
      const mainDocumentUrl = getMainFirestoreUrl(collectionName, docId);
      Logger.log("MAINURL: " + mainDocumentUrl);

      const options = {
        method: 'PATCH',
        contentType: 'application/json',
        payload: JSON.stringify(docData)
      };
      Logger.log("PAYLOAD: " + options.payload);

      try {
        const response = UrlFetchApp.fetch(mainDocumentUrl, options);
        Logger.log(`Document created/updated: ${docId}`);
        Logger.log(`Response: ${response.getContentText()}`);
      } catch (error) {
        Logger.log(`Failed to create/update document ${docId}: ${error}`);
      }
    

      // Create the sub collection after the question document is created
      createSubcollection(docId, lastRowWithData, currentColumnData, sheet);
    }
  }
}
