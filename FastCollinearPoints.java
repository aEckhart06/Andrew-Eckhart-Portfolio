import edu.princeton.cs.algs4.In;

import java.util.ArrayList;
import java.util.Arrays;

public class FastCollinearPoints {
    private int numOfLineSegments;
    private final ArrayList<LineSegment> alLS = new ArrayList<>();


    // finds all line segments containing 4 or more points
    // for each point p, calculate the slope with all other points, q.
    // sort each point with respect to its slope to point p.
    // if three or more points q have equal slope to each other, those points
    // are collinear with point p.
    public FastCollinearPoints(Point[] points) {

        if (points == null) throw new IllegalArgumentException();
        for (int i = 0; i<points.length; i++){
            int j = i;
            while(j>0 && points[j-1].compareTo(points[j]) > 0){
                Point temp = points[j-1];
                points[j-1] = points[j];
                points[j] = temp;
                j--;
            }
        }
        if (points[0] == null) throw new IllegalArgumentException();
        for (int j = 1; j < points.length; j++) {
            if (points[j] == null) throw new IllegalArgumentException();
            if (points[j].compareTo(points[j - 1]) == 0) {
                throw new IllegalArgumentException();
            }
        }
        numOfLineSegments = 0;
        for (Point point : points) {

            Point[] copy = Arrays.copyOf(points, points.length);
            // Sorts copy of original array by slope
            Arrays.sort(copy, point.slopeOrder());

            ArrayList<Point> collinearPoints = new ArrayList<>();
            int consecutiveEqualSlopes = 0;
            for (int j = 0; j < points.length; j++) {
                //Checks corner case at the end of the list of points/slopes.
                //Necessary for vertical cases
                if (j == points.length-2 && consecutiveEqualSlopes >= 2){
                    if (Double.compare(point.slopeTo(copy[j]), point.slopeTo(copy[j + 1])) == 0){
                        collinearPoints.add(copy[j+1]);
                        collinearPoints.add(copy[j]);
                    }

                    //Add original point
                    collinearPoints.add(point);


                    for (int i = 0; i < collinearPoints.size(); i++) {
                        int q = i;
                        Point temp;
                        while (q > 0 && collinearPoints.get(q - 1).compareTo(collinearPoints.get(q)) > 0) {
                            temp = collinearPoints.get(q - 1);
                            collinearPoints.set(q - 1, collinearPoints.get(q));
                            collinearPoints.set(q, temp);
                            q--;
                        }
                    }
                    //Sets the minimum and maximum points in the new line segment
                    Point lo = collinearPoints.get(0);
                    Point hi = collinearPoints.get(collinearPoints.size()-1);
                    LineSegment newSegment = new LineSegment(lo, hi);
                    if (!checkDuplicates(alLS, newSegment)) {
                        numOfLineSegments++;
                        alLS.add(newSegment);

                    }
                    collinearPoints.clear();
                    consecutiveEqualSlopes = 0;
                }

                else if (j<points.length -1 && Double.compare(point.slopeTo(copy[j]), point.slopeTo(copy[j + 1])) == 0) {
                    consecutiveEqualSlopes++;
                    collinearPoints.add(copy[j]);
                    collinearPoints.add(copy[j+1]);
                }

                else if(consecutiveEqualSlopes >= 2){
                        //Adds the original point to the list of current collinear points
                        collinearPoints.add(point);

                        //Sorts the current list of collinear points
                        for (int i = 0; i < collinearPoints.size(); i++) {
                            int q = i;
                            Point temp;
                            while (q > 0 && collinearPoints.get(q - 1).compareTo(collinearPoints.get(q)) > 0) {
                                temp = collinearPoints.get(q - 1);
                                collinearPoints.set(q - 1, collinearPoints.get(q));
                                collinearPoints.set(q, temp);
                                q--;
                            }
                        }
                        //Sets the minimum and maximum points in the new line segment
                        Point lo = collinearPoints.get(0);
                        Point hi = collinearPoints.get(collinearPoints.size()-1);
                        LineSegment newSegment = new LineSegment(lo, hi);
                        //Checks if the new line segment is a duplicate
                        if (!checkDuplicates(alLS, newSegment)) {
                            numOfLineSegments++;
                            alLS.add(newSegment);

                        }
                        collinearPoints.clear();
                        consecutiveEqualSlopes = 0;
                    }
                else if (consecutiveEqualSlopes == 1 || j>=points.length-1) {
                    collinearPoints.clear();
                    consecutiveEqualSlopes = 0;
                }
            }
        }
    }
    private boolean checkDuplicates(ArrayList<LineSegment> lineSegments, LineSegment segment){
        for (LineSegment lineSegment : lineSegments) {
            if (segment.toString().equals(lineSegment.toString())) return true;
        }
        return false;
    }


    private LineSegment[] copy(){
        LineSegment[] lineSegments = new LineSegment[alLS.size()];
        for(int i = 0; i<alLS.size(); i++){
            lineSegments[i] = alLS.get(i);
        }
        return lineSegments;
    }


    // the number of line segments
    public int numberOfSegments(){
        return numOfLineSegments;
    }


    // the line segments

    public LineSegment[] segments(){
        return copy();
    }



    public static void main(String[]args){

        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        FastCollinearPoints fcp = new FastCollinearPoints(points);
        System.out.println(fcp.numberOfSegments());
        for (int i = 0; i<fcp.numberOfSegments(); i++) {
            System.out.println(fcp.segments()[i]);
        }
    }



}



