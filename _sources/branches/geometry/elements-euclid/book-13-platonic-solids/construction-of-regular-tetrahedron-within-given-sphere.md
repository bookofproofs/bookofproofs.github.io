layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-13-platonic-solids
nodeid: bookofproofs$2307
orderid: 1200
parentid: bookofproofs$1885
title: Prop. 13.13: Construction of Regular Tetrahedron within Given Sphere
description: 13.13: CONSTRUCTION OF REGULAR TETRAHEDRON WITHIN GIVEN SPHERE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: construction,dx, 2,given,regular,sphere,tetrahedron,within,x + ct,x - st,y + cp,y + st,y - ct
contributors: @Fitzpatrick,bookofproofs


---


---

### (Proposition 13 from Book 13 of Euclid's “Elements”)

> To construct a (regular) [pyramid][bookofproofs$2221] (i.e., a tetrahedron), and to enclose (it) in a given [sphere][bookofproofs$2223], and to show that the [square][bookofproofs$909] on the [diameter of the sphere][bookofproofs$2226] is one and a half times the [ (square) ][bookofproofs$909] on the side of the [pyramid][bookofproofs$2221].
* Thus, [it is required to construct] a [pyramid][bookofproofs$2221], whose base is [triangle][bookofproofs$6432] `$EFG$`, and apex the [point][bookofproofs$631] `$K$`, from four "equilateral triangles":https://www.bookofproofs.org/branches/equilateral-triangle-isosceles-triangle-scalene-triangle/...
* So, I say that the [square][bookofproofs$909] on the [diameter of the sphere][bookofproofs$2226] is one and a half times the [ (square) ][bookofproofs$909] on the side of the [pyramid][bookofproofs$2221].

![fig13e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book13/fig13e.png?raw=true)

<div style="float:left"><canvas id="cnv" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

§§§1



### Modern Formulation

(not yet contributed)

### Notes

If the [radius][bookofproofs$690] of the [sphere][bookofproofs$2223] is unity then the side of the [pyramid][bookofproofs$2221] (i.e., tetrahedron) is `\[\sqrt{\frac 83}.\]`

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

