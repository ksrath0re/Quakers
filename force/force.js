// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/force.json", function (error, graph) {
    if (error) throw error;

    var link = svg.append("g")
        .attr("class", "links")
//        .attr('fill', 'red')
//        .attr('stroke', 'red')
//        //.attr('stroke-width', function(d) { return d.weight; })
//        .attr("stroke-width", function(d) { return  d.weight;})
        .selectAll("line")
        .data(graph.links)
        .enter().append("line");

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
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
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

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
});

function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}