layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book-13-platonic-solids
nodeid: bookofproofs$2311
orderid: 1600
parentid: bookofproofs$1885
title: Prop. 13.17: Construction of Regular Dodecahedron within Given Sphere
description: 13.17: CONSTRUCTION OF REGULAR DODECAHEDRON WITHIN GIVEN SPHERE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: construction,dodecahedron,dx,2,given,regular,sphere,within,x + ct,x - st,y + cp,y + st,y - ct,dodecahedron construction,regular dodecahedron
contributors: @Fitzpatrick,bookofproofs


---


---

### (Proposition 17 from Book 13 of Euclid's “Elements”)

> To construct a [dodecahedron][bookofproofs$2237], and to enclose (it) in a [sphere][bookofproofs$2223], like the aforementioned figures, and to show that the side of the [dodecahedron][bookofproofs$2237] is that [irrational][bookofproofs$2083] ([straight line][bookofproofs$645]) called an [apotome][bookofproofs$2167].
* Let two [planes][bookofproofs$647] of the aforementioned [cube][bookofproofs$2234] [[Prop. 13.15]][bookofproofs$2309], `$ABCD$` and `$CBEF$`, (which are) at [right angles][bookofproofs$653] to one another, be laid out.
* And let the sides `$AB$`, `$BC$`, `$CD$`, `$DA$`, `$EF$`, `$EB$`, and `$FC$` have each been cut in half at [points][bookofproofs$631] `$G$`, `$H$`, `$K$`, `$L$`, `$M$`, `$N$`, and `$O$` (respectively).
* And let `$GK$`, `$HL$`, `$MH$`, and `$NO$` have been joined.
* And let `$NP$`, `$PO$`, and `$HQ$` have each been cut [in extreme and mean ratio][bookofproofs$1985] at [points][bookofproofs$631] `$R$`, `$S$`, and `$T$` (respectively).
* And let their greater pieces be `$RP$`, `$PS$`, and `$TQ$` (respectively).
* And let `$RU$`, `$SV$`, and `$TW$` have been set up on the exterior side of the [cube][bookofproofs$2234], at [points][bookofproofs$631] `$R$`, `$S$`, and `$T$` (respectively), at [right angles][bookofproofs$653] to the [planes][bookofproofs$647] of the [cube][bookofproofs$2234].
* And let them be made equal to `$RP$`, `$PS$`, and `$TQ$`.
* And let `$UB$`, `$BW$`, `$WC$`, `$CV$`, and `$VU$` have been joined.
* I say that the [pentagon][bookofproofs$6447] `$UBWCV$` is equilateral, and in one [plane][bookofproofs$657], and, further, equiangular.
* ... Thus, if we make the same construction on each of the twelve sides of the [cube][bookofproofs$2234] then some [solid figure][bookofproofs$2210] contained by twelve [equilateral and equiangular pentagon][bookofproofs$6447]s will have been constructed, which is called a [dodecahedron][bookofproofs$2237].
* ... So, I say that the side of the [dodecahedron][bookofproofs$2237] is that [irrational][bookofproofs$2083] [straight line][bookofproofs$645] called an [apotome][bookofproofs$2167].
![fig17e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book13/fig17e.png?raw=true)


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

            for (var i = 0; i < 20; ++i)
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
        for (var i = 0; i < 20; ++i)
            rotate(dod.vertices[i], dod_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();
</script>

