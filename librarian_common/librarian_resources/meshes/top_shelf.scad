translate([-(0.765+0.016),-(0.36+0.016),-(1.235-0.287)]){  
    difference(){
        cube(size=[0.765+0.016*2 ,0.36+0.016, 1.25], center = false);
        
        union(){
            translate([0.016,0.016,1.235-0.287]){
                #cube([0.765,0.5, 0.287], center=false);
                };
                cube([0.765+0.016*2 ,0.36+0.016, 1.25-0.287-0.015], center=false);
        };
    };
};