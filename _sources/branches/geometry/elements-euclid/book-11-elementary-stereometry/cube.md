layout: definition
categories: branches,geometry,elements-euclid,book-11-elementary-stereometry
nodeid: bookofproofs$2234
orderid: 2400
parentid: bookofproofs$1874
title: Def. 11.25: Cube
description: DEF. 11.25: CUBE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: cube,dx, 2,x + ct,x - st,y + cp,y + st,y - ct
contributors: @Fitzpatrick,bookofproofs


---


---

### (Definition 25 from Book 11 of Euclid's “Elements”)

> A **cube** is a [solid figure][bookofproofs$2210] contained by six [equal][bookofproofs$2781] [squares][bookofproofs$909].
### Modern Formulation


A **cube** is (the only)[^1] regular [prism (hexahedron) ][bookofproofs$2222].
<div style="float:left"><canvas id="cnv" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

### Cartesian Coordinates of the Vertices and Faces of a Cube

The Cartesian coordinates `\((x,y,z)\)` of all `\(8\)` vertices of a cube centered at the origin are given by:

`\[\begin{array}{lrrr}
\text{Vertex}&x&y&z\\
	v_{1}&-1&-1&1\\
	v_{2}&-1&-1&-1\\
	v_{3}&1&-1&-1\\
	v_{4}&1&-1&1\\
	v_{5}&1&1&1\\
	v_{6}&1&1&-1\\
	v_{7}&-1&1&-1\\
	v_{8}&-1&1&1\\
\end{array}\]`



The `\(6\)` faces of the octahedron are equilateral triangles with the following vertices:

`\[\begin{array}{lccccc}
\text{Face}\\
f_{1}&v_{1}&v_{2}&v_{3}&v_{4}\\
f_{2}&v_{4}&v_{3}&v_{6}&v_{5}\\
f_{3}&v_{5}&v_{6}&v_{7}&v_{8}\\
f_{4}&v_{8}&v_{7}&v_{2}&v_{1}\\
f_{5}&v_{8}&v_{1}&v_{4}&v_{5}\\
f_{6}&v_{2}&v_{7}&v_{6}&v_{3}\\
\end{array}\]`

[^1]: This will be proven in the [Prop. 18 of Book 13][bookofproofs$2312], thus the cube is well-defined.

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

var Cube = function(center, side) {
    // Generate the vertices
    var d = side/2;

    this.vertices = [
        new Vertex(center.x - d, center.y - d, center.z + d),
        new Vertex(center.x - d, center.y - d, center.z - d),
        new Vertex(center.x + d, center.y - d, center.z - d),
        new Vertex(center.x + d, center.y - d, center.z + d),
        new Vertex(center.x + d, center.y + d, center.z + d),
        new Vertex(center.x + d, center.y + d, center.z - d),
        new Vertex(center.x - d, center.y + d, center.z - d),
        new Vertex(center.x - d, center.y + d, center.z + d)
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^0], this.vertices[^1], this.vertices[^2], this.vertices[^3]],
        [this.vertices[^3], this.vertices[^2], this.vertices[^5], this.vertices[^4]],
        [this.vertices[^4], this.vertices[^5], this.vertices[^6], this.vertices[^7]],
        [this.vertices[^7], this.vertices[^6], this.vertices[^1], this.vertices[^0]],
        [this.vertices[^7], this.vertices[^0], this.vertices[^3], this.vertices[^4]],
        [this.vertices[^1], this.vertices[^6], this.vertices[^5], this.vertices[^2]]
    ];
};

function project(M) {
    return new Vertex2D(M.x, M.z);
}

function render(objects, ctx, dx, dy) {
    // Clear the previous frame
    ctx.clearRect(0, 0, 2*dx, 2*dy);

    // For each object
    for (var i = 0, n_obj = objects.length; i < n_obj; ++i) {
        // For each face
        for (var j = 0, n_faces = objects[i].faces.length; j < n_faces; ++j) {
            // Current face
            var face = objects[i].faces[j];

            // Draw the first vertex
            var P = project(face[^0]);
            ctx.beginPath();
            ctx.moveTo(P.x + dx, -P.y + dy);

            // Draw the other vertices
            for (var k = 1, n_vertices = face.length; k < n_vertices; ++k) {
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

    // Create the cube
    var cube_center = new Vertex(0, 11*dy/10, 0);
    var cube = new Cube(cube_center, dy);
    var objects = [cube];

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

            for (var i = 0; i < 8; ++i)
                rotate(cube.vertices[i], cube_center, theta, phi);

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
        for (var i = 0; i < 8; ++i)
            rotate(cube.vertices[i], cube_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

