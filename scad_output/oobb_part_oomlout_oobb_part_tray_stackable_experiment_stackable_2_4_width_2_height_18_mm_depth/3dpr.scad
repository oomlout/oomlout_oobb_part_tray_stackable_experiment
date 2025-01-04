$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 3]) {
			hull() {
				translate(v = [-25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [-25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
				translate(v = [25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15, r = 5);
				}
			}
		}
		translate(v = [-15.0000000000, 0, 3]) {
			rotate(a = [0, 180, 0]) {
				hull() {
					translate(v = [-10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [-10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
				}
			}
		}
		translate(v = [15.0000000000, 0, 3]) {
			rotate(a = [0, 180, 0]) {
				hull() {
					translate(v = [-10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [-10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
					translate(v = [10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 3, r1 = 3.9500000000, r2 = 2.9500000000);
					}
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 4]) {
			hull() {
				translate(v = [-25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 14, r = 4.2000000000);
				}
				translate(v = [25.0000000000, 10.0000000000, 0]) {
					cylinder(h = 14, r = 4.2000000000);
				}
				translate(v = [-25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 14, r = 4.2000000000);
				}
				translate(v = [25.0000000000, -10.0000000000, 0]) {
					cylinder(h = 14, r = 4.2000000000);
				}
			}
		}
		translate(v = [0, 0, 18]) {
			hull() {
				translate(v = [-24.7500000000, 9.7500000000, 0]) {
					cylinder(h = 3, r = 4.2000000000);
				}
				translate(v = [24.7500000000, 9.7500000000, 0]) {
					cylinder(h = 3, r = 4.2000000000);
				}
				translate(v = [-24.7500000000, -9.7500000000, 0]) {
					cylinder(h = 3, r = 4.2000000000);
				}
				translate(v = [24.7500000000, -9.7500000000, 0]) {
					cylinder(h = 3, r = 4.2000000000);
				}
			}
		}
		translate(v = [-15.0000000000, 0, 1]) {
			#hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
			}
		}
		translate(v = [15.0000000000, 0, 1]) {
			#hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 3, r1 = 2.3500000000, r2 = 3.4000000000);
				}
			}
		}
	}
}