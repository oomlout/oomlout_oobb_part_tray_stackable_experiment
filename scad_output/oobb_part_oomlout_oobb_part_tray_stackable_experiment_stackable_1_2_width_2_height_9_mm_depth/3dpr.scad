$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 3.0000000000]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 5);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 5);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 5);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 5);
				}
			}
		}
		hull() {
			translate(v = [-10.0000000000, 10.0000000000, 0]) {
				cylinder(h = 1.5000000000, r = 3.5000000000);
			}
			translate(v = [10.0000000000, 10.0000000000, 0]) {
				cylinder(h = 1.5000000000, r = 3.5000000000);
			}
			translate(v = [-10.0000000000, -10.0000000000, 0]) {
				cylinder(h = 1.5000000000, r = 3.5000000000);
			}
			translate(v = [10.0000000000, -10.0000000000, 0]) {
				cylinder(h = 1.5000000000, r = 3.5000000000);
			}
		}
		translate(v = [0, 0, 1.5000000000]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
			}
		}
		translate(v = [0, 0, 1.5000000000]) {
			#hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.5000000000, r2 = 4.0000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.5000000000, r2 = 4.0000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.5000000000, r2 = 4.0000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.5000000000, r2 = 4.0000000000);
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 3.0000000000]) {
			#hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 4);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 4);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 4);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 7.5000000000, r = 4);
				}
			}
		}
		translate(v = [0, 0, 9]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.5000000000, r2 = 5.0000000000);
				}
			}
		}
	}
}