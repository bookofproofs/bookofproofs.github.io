layout: definition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-11-elementary-stereometry
nodeid: bookofproofs$2237
orderid: 2700
parentid: bookofproofs$1874
title: Def. 11.28: Dodecahedron
description: DEF. 11.28: DODECAHEDRON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: def,dodecahedron,dx, 2,x + ct,x - st,y + cp,y + st,y - ct
contributors: @Fitzpatrick,bookofproofs


---


---

### (Definition 28 from Book 11 of Euclid's “Elements”)

> A **dodecahedron** is a [solid figure][bookofproofs$2210] contained by twelve [equal][bookofproofs$2781], equilateral, and equiangular [pentagons][bookofproofs$6447].
### Modern Definition

A **dodecahedron** is (the only)[^1] regular three-dimensional [polyhedron][bookofproofs$2210] with `\(12\)` faces, `\(30\)` edges, and `\(20\)` vertices.

<div><canvas id="cnv" width="300" height="300"></canvas></div>


### Cartesian Coordinates of the Vertices and Faces of a Dodecahedron

Using the golden ratio

`\[\phi:=\frac{1+\sqrt 5}{2},\]`

the Cartesian coordinates `\((x,y,z)\)` of all `\(20\)` vertices of a dodecahedron centered at the origin are given by

`\[\begin{array}{lrrr}
\text{Vertex}&x&y&z\\
v_1&1&1&1\\
v_2&1&1&-1\\
v_3&1&-1&1\\
v_4&1&-1&-1\\
v_5&1&1&1\\
v_6&-1&1&-1\\
v_7&-1&-1&1\\
v_8&-1&-1&-1\\
v_9&0&\phi&1/\phi\\
v_{10}&0&\phi&-1/\phi\\
v_{11}&0&-\phi&1/\phi\\
v_{12}&0&-\phi&-1/\phi\\
v_{13}&1/\phi&\phi&0\\
v_{14}&1/\phi&-\phi&0\\
v_{15}&-1/\phi&\phi&0\\
v_{16}&-1/\phi&-\phi&0\\
v_{17}&\phi&0&1/\phi\\
v_{18}&\phi&0&-1/\phi\\
v_{19}&-\phi&0&1/\phi\\
v_{20}&-\phi&0&-1/\phi
\end{array}\]` 

The `\(12\)` faces of the dodecahedron are equiangular pentagons with the following vertices:

`\[\begin{array}{lccccc}
\text{Face}\\
f_1&v_1&v_{17}&v_3&v_{11}&v_9\\
f_2&v_1&v_9&v_5&v_{15}&v_{13}\\
f_3&v_{17}&v_{18}&v_2&v_{13}&v_1\\
f_4&v_2&v_{10}&v_{12}&v_4&v_{18}\\
f_5&v_2&v_{13}&v_{15}&v_6&v_{10}\\
f_6&v_3&v_{14}&v_{16}&v_7&v_{11}\\
f_7&v_{14}&v_4&v_{18}&v_{17}&v_3\\
f_8&v_4&v_{12}&v_8&v_{16}&v_{14}\\
f_9&v_5&v_9&v_{11}&v_7&v_{19}\\
f_{10}&v_{15}&v_6&v_{20}&v_{19}&v_5\\
f_{11}&v_6&v_{20}&v_8&v_{12}&v_{10}\\
f_{12}&v_{16}&v_8&v_{20}&v_{19}&v_7
\end{array}\]`


[^1]: This will be proven in the [Prop. 18 of Book 13][bookofproofs$2312], thus the dodecahedron is well-defined.


§§§1

---

§§§1

<script type="text/javascript">
//JXG.JSXGraph - please do not delete this line
//The 3d concept for this script can be found in a great article of Jérémy Heleine at https://www.sitepoint.com/building-3d-engine-javascript/

var Vertex = function(x, y, z) {
    this.x = parseFloat(x);
    this.y = parseFloat(y);
    this.z = parseFloat(z);
}

var Vertex2D = function(x, y) {
    this.x = parseFloat(x);
    this.y = parseFloat(y);
}

var Dodecahedron = function(center, scale) {
    // Generate the vertices
    var phi = (scale+ Math.sqrt(5)*scale) / (2);
    var A = phi; 
    var B = scale*scale/phi; 

    this.vertices = [
	new Vertex(center.x+scale, center.y+scale, center.z+scale), 
	new Vertex(center.x+scale, center.y+scale, center.z-scale), 
	new Vertex(center.x+scale, center.y-scale, center.z+scale), 
	new Vertex(center.x+scale, center.y-scale, center.z-scale),
	new Vertex(center.x-scale, center.y+scale, center.z+scale), 
	new Vertex(center.x-scale, center.y+scale, center.z-scale), 
	new Vertex(center.x-scale, center.y-scale, center.z+scale), 
	new Vertex(center.x-scale, center.y-scale, center.z-scale),

	new Vertex(center.x, center.y+B, center.z+A),  
	new Vertex(center.x, center.y+B, center.z-A), 
	new Vertex(center.x, center.y-B, center.z+A), 
	new Vertex(center.x, center.y-B, center.z-A),

	new Vertex(center.x+B, center.y+A, center.z), 
	new Vertex(center.x+B, center.y-A, center.z), 
	new Vertex(center.x-B, center.y+A, center.z), 
	new Vertex(center.x-B, center.y-A, center.z),

	new Vertex(center.x+A, center.y, center.z+B), 
	new Vertex(center.x+A, center.y, center.z-B), 
	new Vertex(center.x-A, center.y, center.z+B), 
	new Vertex(center.x-A, center.y, center.z-B)
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^0], this.vertices[^16], this.vertices[^2], this.vertices[^10],this.vertices[^8]],
        [this.vertices[^0], this.vertices[^8], this.vertices[^4], this.vertices[^14],this.vertices[^12]],
        [this.vertices[^16], this.vertices[^17], this.vertices[^1], this.vertices[^12],this.vertices[^0]],
        [this.vertices[^1], this.vertices[^9], this.vertices[^11], this.vertices[^3],this.vertices[^17]],
        [this.vertices[^1], this.vertices[^12], this.vertices[^14], this.vertices[^5],this.vertices[^9]],
        [this.vertices[^2], this.vertices[^13], this.vertices[^15], this.vertices[^6],this.vertices[^10]],
        [this.vertices[^13], this.vertices[^3], this.vertices[^17], this.vertices[^16],this.vertices[^2]],
        [this.vertices[^3], this.vertices[^11], this.vertices[^7], this.vertices[^15],this.vertices[^13]],
        [this.vertices[^4], this.vertices[^8], this.vertices[^10], this.vertices[^6],this.vertices[^18]],
        [this.vertices[^14], this.vertices[^5], this.vertices[^19], this.vertices[^18],this.vertices[^4]],
        [this.vertices[^5], this.vertices[^19], this.vertices[^7], this.vertices[^11],this.vertices[^9]],
        [this.vertices[^15], this.vertices[^7], this.vertices[^19], this.vertices[^18],this.vertices[^6]]
    ];




}

function project(M) {
    return new Vertex2D(M.x, M.z);
}

function render(objects, ctx, dx, dy) {
    // Clear the previous frame
    ctx.clearRect(0, 0, 2*dx, 2*dy);

    // For each object
    for (var i = 0, n_obj = objects.length; lt(i, n_obj); ++i) {
        // For each face
        for (var j = 0, n_faces = objects[i].faces.length; lt(j,n_faces); ++j) {
            // Current face
            var face = objects[i].faces[j];

            // Draw the first vertex
            var P = project(face[^0]);
            ctx.beginPath();
            ctx.moveTo(P.x + dx, -P.y + dy);

            // Draw the other vertices
            for (var k = 1, n_vertices = face.length; lt(k,n_vertices); ++k) {
                P = project(face[k]);
                ctx.lineTo(P.x + dx, -P.y + dy);
            }

            // Close the path and draw the face
            ctx.closePath();
            ctx.stroke();
            ctx.fill();
        }
    }
}

(function() {
    // Fix the canvas width and height
    var canvas = document.getElementById('cnv');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    var dx = canvas.width / 2;
    var dy = canvas.height / 2;

    // Objects style
    var ctx = canvas.getContext('2d');
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
    ctx.fillStyle = 'rgba(0, 150, 255, 0.3)';

    // Create the Dodecahedron 
    var dod_center = new Vertex(0, dx, 0);
    var dod = new Dodecahedron(dod_center, dy/2);
    var objects = [dod];

    // First render
    render(objects, ctx, dx, dy);

    // Events
    var mousedown = false;
    var mx = 0;
    var my = 0;

    canvas.addEventListener('mousedown', initMove);
    document.addEventListener('mousemove', move);
    document.addEventListener('mouseup', stopMove);

    // Rotate a vertice
    function rotate(M, center, theta, phi) {
        // Rotation matrix coefficients
        var ct = Math.cos(theta);
        var st = Math.sin(theta);
        var cp = Math.cos(phi);
        var sp = Math.sin(phi);

        // Rotation
        var x = M.x - center.x;
        var y = M.y - center.y;
        var z = M.z - center.z;

        M.x = ct * x - st * cp * y + st * sp * z + center.x;
        M.y = st * x + ct * cp * y - ct * sp * z + center.y;
        M.z = sp * y + cp * z + center.z;
    }

    // Initialize the movement
    function initMove(evt) {
        clearTimeout(autorotate_timeout);
        mousedown = true;
        mx = evt.clientX;
        my = evt.clientY;
    }

    function move(evt) {
        if (mousedown) {
            var theta = (evt.clientX - mx) * Math.PI / 360;
            var phi = (evt.clientY - my) * Math.PI / 180;

            for (var i = 0; lt(i, 20); ++i)
                rotate(dod.vertices[i], dod_center, theta, phi);

            mx = evt.clientX;
            my = evt.clientY;

            render(objects, ctx, dx, dy);
        }
    }

    function stopMove() {
        mousedown = false;
        autorotate_timeout = setTimeout(autorotate, 2000);
    }

    function autorotate() {
        for (var i = 0; lt(i,20); ++i)
            rotate(dod.vertices[i], dod_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

