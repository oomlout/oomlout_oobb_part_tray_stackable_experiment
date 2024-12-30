$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-2.5000000000, 2.5000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [2.5000000000, 2.5000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [-2.5000000000, -2.5000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [2.5000000000, -2.5000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 3]) {
			#hull() {
				translate(v = [-1.5000000000, 1.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [1.5000000000, 1.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-1.5000000000, -1.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [1.5000000000, -1.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
	}
}