$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
		hull() {
			translate(v = [-2.5000000000, 2.5000000000, 0]) {
				cylinder(h = 1, r = 3.8000000000);
			}
			translate(v = [2.5000000000, 2.5000000000, 0]) {
				cylinder(h = 1, r = 3.8000000000);
			}
			translate(v = [-2.5000000000, -2.5000000000, 0]) {
				cylinder(h = 1, r = 3.8000000000);
			}
			translate(v = [2.5000000000, -2.5000000000, 0]) {
				cylinder(h = 1, r = 3.8000000000);
			}
		}
		translate(v = [0, 0, 1]) {
			hull() {
				translate(v = [-2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [-2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			#hull() {
				translate(v = [-2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 6, r = 3.8000000000);
				}
				translate(v = [2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 6, r = 3.8000000000);
				}
				translate(v = [-2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 6, r = 3.8000000000);
				}
				translate(v = [2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 6, r = 3.8000000000);
				}
			}
		}
		translate(v = [0, 0, 7]) {
			hull() {
				translate(v = [-2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [-2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
				translate(v = [2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 3.8000000000, r2 = 5.0000000000);
				}
			}
		}
		translate(v = [0, 0, 1]) {
			#hull() {
				translate(v = [-2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 2.6000000000, r2 = 3.8000000000);
				}
				translate(v = [2.5000000000, 2.5000000000, 0]) {
					cylinder(h = 1, r1 = 2.6000000000, r2 = 3.8000000000);
				}
				translate(v = [-2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 2.6000000000, r2 = 3.8000000000);
				}
				translate(v = [2.5000000000, -2.5000000000, 0]) {
					cylinder(h = 1, r1 = 2.6000000000, r2 = 3.8000000000);
				}
			}
		}
	}
}