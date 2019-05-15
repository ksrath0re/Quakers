//// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7
////
//var chart2 = d3.select("#area2")
//.append(svg2)

var svg2 = d3.select("#svg2"),
    width = +svg2.attr("width"),
    height = +svg2.attr("height");
//d3.select('body').append('svg2')
var simulation2 = d3.forceSimulation(svg2)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_2_old.json", function (error, graph2) {
    if (error) throw error;

    var link = svg2.append("g")
        .attr("class", "links")
//        .attr('fill', 'red')
//        .attr('stroke', 'red')
//        //.attr('stroke-width', function(d) { return d.weight; })
//        .attr("stroke-width", function(d) { return  d.weight;})
        .selectAll("line")
        .data(graph2.links)
        .enter().append("line");

    var node = svg2.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph2.nodes)
        .enter().append("circle")
        .style("fill", function(d) {
        if (d.class == 1)
        return 'red'
        else
        return 'blue';
  })
        .attr("r", function(d) {
        if (d.degree >= 20 ){return 15}
        else if (d.degree < 20 && d.degree >= 16) {return 12}
        else if (d.degree < 16 && d.degree > 9) {return 10}
        else return d.degree;
  })
        .call(d3.drag()
            .on("start", dragstarted2)
            .on("drag", dragged2)
            .on("end", dragended2));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation2
        .nodes(graph2.nodes)
        .on("tick", ticked);

    simulation2.force("link")
        .links(graph2.links);

    function ticked() {
        link
            .attr("x1", function (d) {
                return d.source.x;
            })
            .attr("y1", function (d) {
                return d.source.y;
            })
            .attr("x2", function (d) {
                return d.target.x;
            })
            .attr("y2", function (d) {
                return d.target.y;
            });

        node
            .attr("cx", function (d) {
                return d.x;
            })
            .attr("cy", function (d) {
                return d.y;
            });
    }
    simulation2.start();
});

function dragstarted2(d) {
    if (!d3.event.active) simulation2.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged2(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended2(d) {
    if (!d3.event.active) simulation2.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}