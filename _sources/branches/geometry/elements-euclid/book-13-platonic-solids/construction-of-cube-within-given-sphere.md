layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-13-platonic-solids
nodeid: bookofproofs$2309
orderid: 1400
parentid: bookofproofs$1885
title: Prop. 13.15: Construction of Cube within Given Sphere
description: 13.15: CONSTRUCTION OF CUBE WITHIN GIVEN SPHERE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: construction,cube,dx, 2,given,sphere,within,x + ct,x - st,y + cp,y + st,y - ct
contributors: bookofproofs,@fitzpatrick

---


---

### (Proposition 15 from Book 13 of Euclid's “Elements”)

> To construct a [cube][bookofproofs$2234], and to enclose (it) in a [sphere][bookofproofs$2223], like in the (case of the) [pyramid][bookofproofs$2221], and to show that the [square][bookofproofs$909] on the [diameter of the sphere][bookofproofs$2226] is three times the [ (square) ][bookofproofs$909] on the side of the [cube][bookofproofs$2234].

![fig15e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book13/fig15e.png?raw=true)

<div style="float:left"><canvas id="cnv" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

§§§1

### Modern Formulation

(not yet contributed)

### Notes

If the [radius][bookofproofs$690] of the [sphere][bookofproofs$2223] is unity then the side of the [cube][bookofproofs$2234] is `\[\sqrt{\frac 43}.\]`

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

