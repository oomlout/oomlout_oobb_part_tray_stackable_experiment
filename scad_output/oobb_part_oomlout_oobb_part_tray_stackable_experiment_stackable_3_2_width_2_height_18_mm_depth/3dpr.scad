$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 1]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 17, r = 5);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 17, r = 5);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 17, r = 5);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 17, r = 5);
				}
			}
		}
		translate(v = [0.0000000000, 0.0000000000, 0.5000000000]) {
			rotate(a = [0, 180, 0]) {
				hull() {
					translate(v = [-10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 0.5000000000, r1 = 3.5000000000, r2 = 3.0000000000);
					}
					translate(v = [10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 0.5000000000, r1 = 3.5000000000, r2 = 3.0000000000);
					}
					translate(v = [-10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 0.5000000000, r1 = 3.5000000000, r2 = 3.0000000000);
					}
					translate(v = [10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 0.5000000000, r1 = 3.5000000000, r2 = 3.0000000000);
					}
				}
			}
		}
		translate(v = [0.0000000000, 0.0000000000, 1.5000000000]) {
			rotate(a = [0, 180, 0]) {
				hull() {
					translate(v = [-10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 1, r1 = 3.5000000000, r2 = 3.5000000000);
					}
					translate(v = [10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 1, r1 = 3.5000000000, r2 = 3.5000000000);
					}
					translate(v = [-10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 1, r1 = 3.5000000000, r2 = 3.5000000000);
					}
					translate(v = [10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 1, r1 = 3.5000000000, r2 = 3.5000000000);
					}
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 3]) {
			hull() {
				translate(v = [-10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15, r = 3.5000000000);
				}
				translate(v = [10.0000000000, 10.0000000000, 0]) {
					cylinder(h = 15, r = 3.5000000000);
				}
				translate(v = [-10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15, r = 3.5000000000);
				}
				translate(v = [10.0000000000, -10.0000000000, 0]) {
					cylinder(h = 15, r = 3.5000000000);
				}
			}
		}
		translate(v = [0.0000000000, 0.0000000000, 3.5000000000]) {
			rotate(a = [0, 180, 0]) {
				hull() {
					translate(v = [-10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 1.5000000000, r1 = 2.0000000000, r2 = 2.0000000000);
					}
					translate(v = [10.0000000000, 10.0000000000, 0]) {
						cylinder(h = 1.5000000000, r1 = 2.0000000000, r2 = 2.0000000000);
					}
					translate(v = [-10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 1.5000000000, r1 = 2.0000000000, r2 = 2.0000000000);
					}
					translate(v = [10.0000000000, -10.0000000000, 0]) {
						cylinder(h = 1.5000000000, r1 = 2.0000000000, r2 = 2.0000000000);
					}
				}
			}
		}
		#translate(v = [-12.3000000000, -17.6250000000, 1]) {
			cube(size = [0.6000000000, 5.2500000000, 0.2500000000]);
		}
		#translate(v = [-12.3000000000, 12.3750000000, 1]) {
			cube(size = [0.6000000000, 5.2500000000, 0.2500000000]);
		}
		#translate(v = [-11.1000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-11.1000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-9.9000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-9.9000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-8.7000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-8.7000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-7.5000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-7.5000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-6.3000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-6.3000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-5.1000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-5.1000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-3.9000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-3.9000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-2.7000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-2.7000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-1.5000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-1.5000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-0.3000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [-0.3000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [0.9000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [0.9000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [2.1000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [2.1000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [3.3000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [3.3000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [4.5000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [4.5000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [5.7000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [5.7000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [6.9000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [6.9000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [8.1000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [8.1000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [9.3000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [9.3000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [10.5000000000, -16.7500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [10.5000000000, 13.2500000000, 1]) {
			cube(size = [0.6000000000, 3.5000000000, 0.2500000000]);
		}
		#translate(v = [11.7000000000, -17.6250000000, 1]) {
			cube(size = [0.6000000000, 5.2500000000, 0.2500000000]);
		}
		#translate(v = [11.7000000000, 12.3750000000, 1]) {
			cube(size = [0.6000000000, 5.2500000000, 0.2500000000]);
		}
		#translate(v = [-18.5000000000, -12.3000000000, 1]) {
			cube(size = [7.0000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [11.5000000000, -12.3000000000, 1]) {
			cube(size = [7.0000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -11.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -11.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -9.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -9.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -8.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -8.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -7.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -7.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -6.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -6.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -5.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -5.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -3.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -3.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -2.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -2.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -1.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -1.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, -0.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, -0.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 0.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 0.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 2.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 2.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 3.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 3.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 4.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 4.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 5.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 5.7000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 6.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 6.9000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 8.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 8.1000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 9.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 9.3000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-16.7500000000, 10.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [13.2500000000, 10.5000000000, 1]) {
			cube(size = [3.5000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-18.5000000000, 11.7000000000, 1]) {
			cube(size = [7.0000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [11.5000000000, 11.7000000000, 1]) {
			cube(size = [7.0000000000, 0.6000000000, 0.2500000000]);
		}
		#translate(v = [-17.2500000000, -17.2500000000, 1]) {
			cube(size = [4.5000000000, 4.5000000000, 0.2500000000]);
		}
		#translate(v = [12.7500000000, -17.2500000000, 1]) {
			cube(size = [4.5000000000, 4.5000000000, 0.2500000000]);
		}
		#translate(v = [-17.2500000000, 12.7500000000, 1]) {
			cube(size = [4.5000000000, 4.5000000000, 0.2500000000]);
		}
		#translate(v = [12.7500000000, 12.7500000000, 1]) {
			cube(size = [4.5000000000, 4.5000000000, 0.2500000000]);
		}
		#translate(v = [-16.2500000000, -16.2500000000, 1.2500000000]) {
			cube(size = [2.5000000000, 2.5000000000, 0.2500000000]);
		}
		#translate(v = [13.7500000000, -16.2500000000, 1.2500000000]) {
			cube(size = [2.5000000000, 2.5000000000, 0.2500000000]);
		}
		#translate(v = [-16.2500000000, 13.7500000000, 1.2500000000]) {
			cube(size = [2.5000000000, 2.5000000000, 0.2500000000]);
		}
		#translate(v = [13.7500000000, 13.7500000000, 1.2500000000]) {
			cube(size = [2.5000000000, 2.5000000000, 0.2500000000]);
		}
	}
}