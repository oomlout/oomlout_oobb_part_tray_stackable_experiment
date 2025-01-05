$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-25.0000000000, 10.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [25.0000000000, 10.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [-25.0000000000, -10.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [25.0000000000, -10.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 3]) {
			#hull() {
				translate(v = [-23.5000000000, 8.5000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [23.5000000000, 8.5000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [-23.5000000000, -8.5000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [23.5000000000, -8.5000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
			}
		}
	}
}