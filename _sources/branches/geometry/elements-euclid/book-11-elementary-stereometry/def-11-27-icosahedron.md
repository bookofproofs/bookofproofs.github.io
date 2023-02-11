layout: definition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-11-elementary-stereometry
nodeid: bookofproofs$2236
orderid: 2600
parentid: bookofproofs$1874
title: Def. 11.27: Icosahedron
description: DEF. 11.27: ICOSAHEDRON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: def,dx, 2,icosahedron,x + ct,x - st,y + cp,y + st,y - ct
contributors: @Fitzpatrick,bookofproofs


---


---

### (Definition 27 from Book 11 of Euclid's “Elements”)

> An **icosahedron** is a [solid figure][bookofproofs$2210] contained by twenty [equal][bookofproofs$2781] and [equilateral triangles][bookofproofs$688].
### Modern Definition

An **icosahedron** is (the only)[^1] regular three-dimensional [polyhedron][bookofproofs$2210] with `\(20\)` faces, `\(30\)` edges, and `\(12\)` vertices.



<canvas id="cnv15349" class='centered' width="300" height="300"></canvas>
<div style="clear:both"></div> 



### Cartesian Coordinates of the Vertices and Faces of an Icosahedron

Using the golden ratio

`\[\phi:=\frac{1+\sqrt 5}{2},\]`

the Cartesian coordinates `\((x,y,z)\)` of all `\(12\)` vertices of the icosahedron centered at the origin are given by

`\[\begin{array}{lrrr}
\text{Vertex}&x&y&z\\
	v_{1}&-1&0&\phi\\
	v_{2}&1&0&\phi\\
	v_{3}&-1&0&-\phi\\
	v_{4}&1&0&-\phi\\
	v_{5}&0&\phi&1\\
	v_{6}&0&\phi&-1\\
	v_{7}&0&-\phi&1\\
	v_{8}&0&-\phi&-1\\
	v_{9}&\phi&1&0\\
	v_{10}&-\phi&1&0\\
	v_{11}&\phi&-1&0\\
	v_{12}&-\phi&-1&0
\end{array}\]`

The `\(20\)` faces of the icosahedron are equiangular triangles with the following vertices:

`\[\begin{array}{lccccc}
\text{Face}\\
f_{1}&v_{1}&v_{2}&v_{5}\\
f_{2}&v_{1}&v_{2}&v_{7}\\
f_{3}&v_{1}&v_{5}&v_{10}\\
f_{4}&v_{1}&v_{7}&v_{12}\\
f_{5}&v_{1}&v_{10}&v_{12}\\
f_{6}&v_{2}&v_{7}&v_{11}\\
f_{7}&v_{2}&v_{5}&v_{9}\\
f_{8}&v_{3}&v_{4}&v_{6}\\
f_{9}&v_{3}&v_{4}&v_{8}\\
f_{10}&v_{3}&v_{6}&v_{10}\\
f_{11}&v_{3}&v_{8}&v_{12}\\
f_{12}&v_{3}&v_{10}&v_{12}\\
f_{13}&v_{4}&v_{6}&v_{9}\\
f_{14}&v_{4}&v_{9}&v_{11}\\
f_{15}&v_{4}&v_{11}&v_{8}\\
f_{16}&v_{5}&v_{6}&v_{9}\\
f_{17}&v_{5}&v_{6}&v_{10}\\
f_{18}&v_{7}&v_{8}&v_{12}\\
f_{19}&v_{7}&v_{8}&v_{11}\\
f_{20}&v_{2}&v_{9}&v_{11}\\
\end{array}\]`


[^1]: This will be proven in the [Prop. 18 of Book 13][bookofproofs$2312], thus the icosahedron is well-defined.


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
};

var Vertex2D = function(x, y) {
    this.x = parseFloat(x);
    this.y = parseFloat(y);
};

var Icosahedron = function(center, scale) {
    // Generate the vertices
    var phi = (scale+ Math.sqrt(5)*scale) / (2);

    this.vertices = [
	new Vertex(center.x-scale, center.y, center.z+phi),
	new Vertex(center.x+scale, center.y, center.z+phi),
	new Vertex(center.x-scale, center.y, center.z-phi),
	new Vertex(center.x+scale, center.y, center.z-phi),
	new Vertex(center.x, center.y+phi, center.z+scale),
	new Vertex(center.x, center.y+phi, center.z-scale),
	new Vertex(center.x, center.y-phi, center.z+scale),
	new Vertex(center.x, center.y-phi, center.z-scale),
	new Vertex(center.x+phi, center.y+scale, center.z),
	new Vertex(center.x-phi, center.y+scale, center.z),
	new Vertex(center.x+phi, center.y-scale, center.z),
	new Vertex(center.x-phi, center.y-scale, center.z)
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^0], this.vertices[^1], this.vertices[^4]],
        [this.vertices[^0], this.vertices[^1], this.vertices[^6]],
        [this.vertices[^0], this.vertices[^4], this.vertices[^9]],
        [this.vertices[^0], this.vertices[^6], this.vertices[^11]],
        [this.vertices[^0], this.vertices[^9], this.vertices[^11]],
        [this.vertices[^1], this.vertices[^6], this.vertices[^10]],
        [this.vertices[^1], this.vertices[^4], this.vertices[^8]],
        [this.vertices[^2], this.vertices[^3], this.vertices[^5]],
        [this.vertices[^2], this.vertices[^3], this.vertices[^7]],
        [this.vertices[^2], this.vertices[^5], this.vertices[^9]],
        [this.vertices[^2], this.vertices[^7], this.vertices[^11]],
        [this.vertices[^2], this.vertices[^9], this.vertices[^11]],
        [this.vertices[^3], this.vertices[^5], this.vertices[^8]],
        [this.vertices[^3], this.vertices[^8], this.vertices[^10]],
        [this.vertices[^3], this.vertices[^10], this.vertices[^7]],
        [this.vertices[^4], this.vertices[^5], this.vertices[^8]],
        [this.vertices[^4], this.vertices[^5], this.vertices[^9]],
        [this.vertices[^6], this.vertices[^7], this.vertices[^11]],
        [this.vertices[^6], this.vertices[^7], this.vertices[^10]],
        [this.vertices[^1], this.vertices[^8], this.vertices[^10]],
    ];




};

function project(M) {
    return new Vertex2D(M.x, M.z);
}

function render(objects, ctx, dx, dy) {
    // Clear the previous frame
    ctx.clearRect(0, 0, 2*dx, 2*dy);

    // For each object
    for (var i = 0, n_obj = objects.length; lt(i , n_obj); ++i) {
        // For each face
        for (var j = 0, n_faces = objects[i].faces.length; lt(j , n_faces); ++j) {
            // Current face
            var face = objects[i].faces[j];

            // Draw the first vertex
            var P = project(face[^0]);
            ctx.beginPath();
            ctx.moveTo(P.x + dx, -P.y + dy);
            // Draw the other vertices
            for (var k = 1, n_vertices = face.length; lt(k , n_vertices); ++k) {
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
    var canvas = document.getElementById('cnv15349');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    var dx = canvas.width / 2;
    var dy = canvas.height / 2;

    // Objects style
    var ctx = canvas.getContext('2d');
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
    ctx.fillStyle = 'rgba(0, 150, 255, 0.3)';

    // Create the Icosahedron
    var ico_center = new Vertex(0, dx, 0);
    var ico = new Icosahedron(ico_center, dy/2);
    var objects = [ico];

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

            for (var i = 0; lt(i , 12); ++i)
                rotate(ico.vertices[i], ico_center, theta, phi);

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
        for (var i = 0; lt(i , 12); ++i)
            rotate(ico.vertices[i], ico_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

