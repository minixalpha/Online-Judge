package ios.ac.cn;

import java.util.HashMap;
import java.util.Map;

class Point {
	int x;
	int y;

	Point() {
		x = 0;
		y = 0;
	}

	Point(int a, int b) {
		x = a;
		y = b;
	}
}

/**
 * 注意边界条件，　点数目为0, 1时算法是否成立
 * 
 * 语法坑 Double d1 = new Double(0.0); Double d2 = new Double(-0.0);
 * System.out.println(d1.equals(d2)); false
 * 
 * @author zhaoxk
 * 
 */
public class MaxPointsonaLine {
	public int maxPoints(Point[] points) {
		int max = 0;
		for (int i = 0; i < points.length; i++) {
			int samePointCount = 0;
			int curMax = 0;
			Map<Double, Integer> arcNum = new HashMap<>();
			for (int j = i + 1; j < points.length; j++) {
				if (isSame(points[i], points[j])) {
					samePointCount++;
				} else {
					double arc = getArc(points[i], points[j]);
					if (arcNum.containsKey(arc)) {
						arcNum.put(arc, arcNum.get(arc) + 1);
					} else {
						arcNum.put(arc, 1);
					}
					curMax = Math.max(curMax, arcNum.get(arc));
				}
			}
			max = Math.max(max, samePointCount + curMax + 1);
		}

		return max;
	}

	private boolean isSame(Point p, Point q) {
		return p.x == q.x && p.y == q.y;
	}

	private double getArc(Point p, Point q) {
		if (p.y == q.y) {
			return Double.NaN;
		} else {
			double arc = 1.0 * (p.x - q.x) / (p.y - q.y);
			if (arc == -0.0) {
				return 0.0;
			} else {
				return arc;
			}
		}
	}

	public static void main(String[] args) {
		MaxPointsonaLine mp = new MaxPointsonaLine();
		Point[] points = { new Point(4, 0), new Point(4, -1), new Point(4, 5) };
		System.out.println(mp.maxPoints(points));
	}
}
