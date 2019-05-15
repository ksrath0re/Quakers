// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg2_new = d3.select("#svg2_new"),
    width = +svg2_new.attr("width"),
    height = +svg2_new.attr("height");

//d3.select('body').append('svg2_new')
var simulation2_new = d3.forceSimulation(svg2_new)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_2_new.json", function (error, graph2_new) {
    if (error) throw error;

    var link = svg2_new.append("g")
        .attr("class", "links")
//        .attr('fill', 'red')
//        .attr('stroke', 'red')
//        //.attr('stroke-width', function(d) { return d.weight; })
//        .attr("stroke-width", function(d) { return  d.weight;})
        .selectAll("line")
        .data(graph2_new.links)
        .enter().append("line");

    var node = svg2_new.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph2_new.nodes)
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
            .on("start", dragstarted2_new)
            .on("drag", dragged2_new)
            .on("end", dragended2_new));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

//    var label = svg2_new.selectAll("nodes")
//    .data(graph2_new.nodes)
//    .enter()
//    .append("text")
//    .text(function (d) { return d.id; })
//    .style("text-anchor", "middle")
//    .style("fill", "#555")
//    .style("font-family", "Arial")
//    .style("font-size", 9);

    simulation2_new
        .nodes(graph2_new.nodes)
        .on("tick", ticked);

    simulation2_new.force("link")
        .links(graph2_new.links);

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

//        label.attr("x", function(d){ return d.x; })
//    			 .attr("y", function (d) {return d.y - 10; });
    }
});

function dragstarted2_new(d) {
    if (!d3.event.active) simulation2_new.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged2_new(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended2_new(d) {
    if (!d3.event.active) simulation2_new.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}
