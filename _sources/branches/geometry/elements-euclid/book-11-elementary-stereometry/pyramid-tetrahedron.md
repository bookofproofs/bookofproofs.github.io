layout: definition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-11-elementary-stereometry
nodeid: bookofproofs$2221
orderid: 1100
parentid: bookofproofs$1874
title: Def. 11.12: Pyramid, Tetrahedron
description: DEF. 11.12: PYRAMID, TETRAHEDRON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: 1.5, center.y + scale,base,dx, 2,pyramid,tetrahedron,top,x + ct,x - st,y + cp,y + st,y - ct
contributors: bookofproofs,@fitzpatrick


---


---



> A **pyramid** is a [solid figure][bookofproofs$2210], contained by [planes][bookofproofs$647], (which is) constructed from one [plane][bookofproofs$647] to one [point][bookofproofs$631].
### Modern Formulation

A **pyramid** is a three-dimensional [polyhedron[solid figure][bookofproofs$2210] with a designated face called the **base** of the pyramid and one designated vertex, which is not on the base, called the **top** of the pyramid. All other faces of the pyramid are constructed as triangles between the sides of the base and the top. Depending on the number `\(n\)` of the vertices  of the base, the pyramid will have `\(n+1\)` faces (i.e. `\(n\)` triangular faces and one base), `\(n+1\)` vertices (i.e. `\(n\)` vertices of the base and one top) and `\(2n\)` edges (i.e. `\(n\)` edges of the base and `\(n\)` edges from drawn from the vertices of the base to the top).

<div style="float:left"><canvas id="cnv1" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

A **tetrahedron** is (the only)[^1] regular pyramid.

<div style="float:left"><canvas id="cnv" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

### Cartesian Coordinates of the Vertices and Faces of a Tetrahedron

The Cartesian coordinates `\((x,y,z)\)` of all `\(4\)` vertices of a tetrahedron centered at the origin are given by:

`\[\begin{array}{lrrr}
\text{Vertex}&x&y&z\\
	v_{1}&1&1&1\\
	v_{2}&-1&-1&1\\
	v_{3}&-1&1&-1\\
	v_{4}&1&-1&-1\\
\end{array}\]`


The `\(4\)` faces of the tetrahedron are equilateral triangles with the following vertices:

`\[\begin{array}{lccccc}
\text{Face}\\
f_{1}&v_{1}&v_{2}&v_{3}\\
f_{2}&v_{1}&v_{2}&v_{4}\\
f_{3}&v_{1}&v_{3}&v_{4}\\
f_{4}&v_{2}&v_{3}&v_{4}\\
\end{array}\]`

[^1]: This will be proven in the [Prop. 18 of Book 13][bookofproofs$2312], thus the tetrahedron is well-defined.

§§§1





§§§2

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

var Tetrahedron = function(center, scale) {
    // Generate the vertices
    scale=scale/2;

    this.vertices = [
        new Vertex(center.x + scale, center.y + scale, center.z + scale),
        new Vertex(center.x - scale, center.y - scale, center.z + scale),
        new Vertex(center.x - scale, center.y + scale, center.z - scale),
        new Vertex(center.x + scale, center.y - scale, center.z - scale),
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^0], this.vertices[^1], this.vertices[^3]],
        [this.vertices[^0], this.vertices[^1], this.vertices[^2]],
        [this.vertices[^0], this.vertices[^2], this.vertices[^3]],
        [this.vertices[^1], this.vertices[^2], this.vertices[^3]],
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

    // Create the Tetrahedron
    var tet_center = new Vertex(0, 11*dy/10, 0);
    var tet = new Tetrahedron(tet_center, dy);
    var objects = [tet];

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

            for (var i = 0; i < 4; ++i)
                rotate(tet.vertices[i], tet_center, theta, phi);

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
        for (var i = 0; i < 4; ++i)
            rotate(tet.vertices[i], tet_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>


§§§2

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

var Tetrahedron = function(center, scale) {
    // Generate the vertices
    scale=scale/2;

    this.vertices = [
        new Vertex(center.x, center.y, center.z),
        new Vertex(center.x, center.y, center.z + scale),
        new Vertex(center.x, center.y+scale, center.z),
        new Vertex(center.x, center.y + scale, center.z + scale),
        new Vertex(center.x + scale*1.5, center.y + scale*.5, center.z + scale*.5),
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^1], this.vertices[^0], this.vertices[^2], this.vertices[^3]],
        [this.vertices[^4], this.vertices[^1], this.vertices[^0]],
        [this.vertices[^4], this.vertices[^1], this.vertices[^3]],
        [this.vertices[^4], this.vertices[^3], this.vertices[^2]],
        [this.vertices[^4], this.vertices[^2], this.vertices[^0]],
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
    var canvas = document.getElementById('cnv1');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    var dx = canvas.width / 2;
    var dy = canvas.height / 2;

    // Objects style
    var ctx = canvas.getContext('2d');
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
    ctx.fillStyle = 'rgba(0, 150, 255, 0.3)';

    // Create the Tetrahedron
    var tet_center = new Vertex(0, 11*dy/10, 0);
    var tet = new Tetrahedron(tet_center, dy);
    var objects = [tet];

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

            for (var i = 0; i < 5; ++i)
                rotate(tet.vertices[i], tet_center, theta, phi);

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
        for (var i = 0; i < 5; ++i)
            rotate(tet.vertices[i], tet_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

