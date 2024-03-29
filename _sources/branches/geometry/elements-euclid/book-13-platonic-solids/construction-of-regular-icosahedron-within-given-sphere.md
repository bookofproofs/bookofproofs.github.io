layout: proposition
categories: branches,geometry,elements-euclid,book-13-platonic-solids
nodeid: bookofproofs$2310
orderid: 1500
parentid: bookofproofs$1885
title: Prop. 13.16: Construction of Regular Icosahedron within Given Sphere
description: 13.16: CONSTRUCTION OF REGULAR ICOSAHEDRON WITHIN GIVEN SPHERE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: construction,dx,2,given,icosahedron,regular,sphere,within,x + ct,x - st,y + cp,y + st,y - ct,regular icosahedron
contributors: @Fitzpatrick,bookofproofs

---


---

### (Proposition 16 from Book 13 of Euclid's “Elements”)

> To construct an [icosahedron][bookofproofs$2236], and to enclose (it) in a [sphere][bookofproofs$2223], like the aforementioned figures, and to show that the side of the [icosahedron][bookofproofs$2236] is that [irrational][bookofproofs$2083] ([straight line][bookofproofs$645]) called [minor][bookofproofs$2170].
![fig16ae](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book13/fig16ae.png?raw=true)


![fig16e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book13/fig16e.png?raw=true)

<div style="float:left"><canvas id="cnv" width="300" height="300"></canvas></div>
<div style="clear:both"></div>

§§§1

### Modern Formulation

(not yet contributed)

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

            for (var i = 0; i < 12; ++i)
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
        for (var i = 0; i < 12; ++i)
            rotate(ico.vertices[i], ico_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

