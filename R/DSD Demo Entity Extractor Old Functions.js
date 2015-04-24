// Adds all the entities to the datatable.
    function addEntityDetails(inputArr) {

        for (var i = 0, len = inputArr.length; i < len; i += 5) {
            var textArticle = inputArr[i];
            var textMention = inputArr[i + 1];
            var textOffset = inputArr[i + 2];
            var textLength = inputArr[i + 3]
            var textTypeCode = inputArr[i + 4];

            var textTypeSpan = getTextTypeSpan(textTypeCode);
            
            // Plots the details table.
            var textMentionSpan = '<span class="bold theme-font">' + textMention + "</span>";
            entityDetailsTable.row.add([
                textArticle,
                textMentionSpan,
                textOffset,
                textLength,
                textTypeSpan
            ]).draw();
        }
    }

    // Populates the entity summary table with the entity dictionary.
    function addEntitySummary(entityDict) {
        for (key in entityDict) {
            entitySummaryTable.row.add([
                entityDict[key].entity,
                getTextTypeSpan(entityDict[key].type),
                entityDict[key].quantity
            ]).draw();
        }
    };

    // Graphs the occurance of each entity type in a given entity dictionary.
    function graphEntityTypeFrequency(entityDict) {

        // Counts each type instance.
        var entityTypeDict = {};
        for (key in entityDict) {
            var entityType = entityDict[key].type;
            if (entityTypeDict.hasOwnProperty(entityType)) {
                entityTypeDict[entityType] += entityDict[key].quantity;
            } else {
                entityTypeDict[entityType] = 1;
            }
        };

        // Converts the type count to graph data.
        var graphData = []
        for (key in entityTypeDict) {
            if (key === 'LOC') {
                var typeData = ["Location", entityTypeDict[key]]
            } else if (key === 'PER') {
                var typeData = ["Person", entityTypeDict[key]]
            } else if (key === 'ORG') {
                var typeData = ["Organization", entityTypeDict[key]]
            } else {
                var typeData = [key, entityTypeDict[key]]
            }
            
            graphData.push(typeData);
        }
        
        // Plots bar graph
        if (graphData.length > 0) {
            $('#entityFrequencyGraph').addClass('entityFrequencyGraph');
            $.plot("#entityFrequencyGraph", [graphData], {
                series: {
                    bars: {
                        show: true,
                        barWidth: 0.3,
                        align: "center"
                    }
                },
                xaxis: {
                    mode: "categories",
                    tickLength: 0
                },
                colors: ["#45b6af"]
            });
        }
    };

    // Graphs the entity frequency in a graph. 
    function graphEnityFrequency(entityDict) {
        $('#entityFrequencyGraph').addClass('entityFrequencyGraph');
        // Populates frequency data from the entity dictionary.
        var graphData = [];
        for (key in entityDict) {
            var entityName = entityDict[key].entity;
            var entityQuantity = entityDict[key].quantity;
            var entityData = [];
            entityData[0] = entityName;
            entityData[1] = entityQuantity;
            graphData.push(entityData);
        }
        $.plot("#entityFrequencyGraph", [graphData], {
            series: {
                bars: {
                    show: true,
                    barWidth: 0.3,
                    align: "center"
                }
            },
            xaxis: {
                mode: "categories",
                tickLength: 0
            },
            colors: ["#45b6af"]
        });
    };