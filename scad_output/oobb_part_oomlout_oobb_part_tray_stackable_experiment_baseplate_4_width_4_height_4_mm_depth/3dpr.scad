$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-25.0000000000, 25.0000000000, 0]) {
				cylinder(h = 4, r = 5);
			}
			translate(v = [25.0000000000, 25.0000000000, 0]) {
				cylinder(h = 4, r = 5);
			}
			translate(v = [-25.0000000000, -25.0000000000, 0]) {
				cylinder(h = 4, r = 5);
			}
			translate(v = [25.0000000000, -25.0000000000, 0]) {
				cylinder(h = 4, r = 5);
			}
		}
	}
	union() {
		translate(v = [-15.0000000000, -15.0000000000, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
			}
		}
		translate(v = [-15.0000000000, 15.0000000000, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
			}
		}
		translate(v = [15.0000000000, -15.0000000000, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
			}
		}
		translate(v = [15.0000000000, 15.0000000000, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 2.5000000000, r = 4.3000000000);
				}
			}
		}
	}
}