$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 3.0000000000]) {
			hull() {
				translate(v = [-25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 16.5000000000, r = 5);
				}
				translate(v = [25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 16.5000000000, r = 5);
				}
				translate(v = [-25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 16.5000000000, r = 5);
				}
				translate(v = [25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 16.5000000000, r = 5);
				}
			}
		}
		translate(v = [-15.0000000000, 0, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
			}
		}
		translate(v = [15.0000000000, 0, 0]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r = 3.7500000000);
				}
			}
		}
		translate(v = [-15.0000000000, 0, 1.5000000000]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
			}
		}
		translate(v = [15.0000000000, 0, 1.5000000000]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 3.7500000000, r2 = 5.0000000000);
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 4.5000000000]) {
			hull() {
				translate(v = [-25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15.5000000000, r = 4);
				}
				translate(v = [25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15.5000000000, r = 4);
				}
				translate(v = [-25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15.5000000000, r = 4);
				}
				translate(v = [25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15.5000000000, r = 4);
				}
			}
		}
		translate(v = [-15.3750000000, 0, 3.5000000000]) {
			#hull() {
				translate(v = [-9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [-9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
			}
		}
		translate(v = [15.3750000000, 0, 3.5000000000]) {
			#hull() {
				translate(v = [-9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [-9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
				translate(v = [9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1, r = 4);
				}
			}
		}
		translate(v = [0, 0, 18]) {
			hull() {
				translate(v = [-24.7500000000, 9.7500000000, 0]) {
					cylinder(h = 1.5000000000, r = 4);
				}
				translate(v = [24.7500000000, 9.7500000000, 0]) {
					cylinder(h = 1.5000000000, r = 4);
				}
				translate(v = [-24.7500000000, -9.7500000000, 0]) {
					cylinder(h = 1.5000000000, r = 4);
				}
				translate(v = [24.7500000000, -9.7500000000, 0]) {
					cylinder(h = 1.5000000000, r = 4);
				}
			}
		}
		translate(v = [-15.3750000000, 0, 2.0000000000]) {
			#hull() {
				translate(v = [-9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [-9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
			}
		}
		translate(v = [15.3750000000, 0, 2.0000000000]) {
			#hull() {
				translate(v = [-9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [9.6250000000, 10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [-9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
				translate(v = [9.6250000000, -10.0000000000, 0]) {
					cylinder(h = 1.5000000000, r1 = 2.7500000000, r2 = 4.0000000000);
				}
			}
		}
	}
}