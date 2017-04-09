var cy;


$(function(){

  cy = cytoscape({
    
                    container: document.getElementById('cy'),
                    ready: function(){
                    },
                    layout: {
                        name: 'grid',
                        rows: 2,
                        cols: 2
                    },
                    style: [
                        {
                            selector: 'node',
              style: {
                shape: 'round',
                'background-color': '#808000',
                label: 'data(id)',
                'text-valign': 'center',
            'color': 'white',
            'text-outline-width': 1,
            'text-outline-color': 'black'
                            }
                        },
                        {
                            selector: '.edgehandles-hover',
                            css: {
                                'background-color': 'red'
                            }
                        },
                        {
                            selector: '.edgehandles-source',
                            css: {
                                'border-width': 2,
                                'border-color': 'red'
                            }
                        },
                        {
                            selector: '.edgehandles-target',
                            css: {
                                'border-width': 2,
                                'border-color': 'red'
                            }
                        },
                        {
                            selector: '.edgehandles-preview, .edgehandles-ghost-edge',
                            css: {
                                'line-color': 'red',
                                'target-arrow-color': 'red',
                                'source-arrow-color': 'red'
                            }
                        }
                    ]
  });

      cy.edgehandles({
   toggleOffOnLeave: true,
   handleNodes: "node",
   handleSize: 10,
   edgeType: function(){ return 'flat'; }
 });
    var i = 0;
    var del_elem = [];
    cy.on('cxttap', 'node' ,function (evt) {
        cy.remove(cy.$("#" + evt.cyTarget.id()));
        del_elem[del_elem.length] = evt.cyTarget.id();
    });
    cy.on('cxttap', 'edge' ,function (evt) {
        cy.remove(cy.$("#" + evt.cyTarget.id()));
    });
    var can = true;
    $('.cytosc').on('tap', '*',function(e) {

            if(del_elem.length == 0) {
                i += 1;
                index = i;
            } else {
                del_elem = del_elem.sort();
                index = del_elem[0];
                del_elem.splice(0,1);
            }
            cy.add([{
                group : "nodes",

                data : {
                    id : index
                },
                renderedPosition : {
                    x: e.pageX,
                    y: e.pageY
                }

            }]);
    });
  var $config = $('#config');
  var $btnParam = $('<div class="param"></div>');
  $config.append( $btnParam );
  var buttons = [
    {
      label: '<i class="fa fa-eye"></i>',
    },
    {
      label: '<i class="fa fa-remove"></i>'
    },
    {
      label: '<i class="fa fa-check"></i>'
    }
  ];
  buttons.forEach( makeButton );

function makeButton( opts ){
    var $button = $('<button class="btn btn-default">'+ opts.label +'</button>');
    
    $btnParam.append( $button );

    $button.on('click', function(){
      alert("123");

      if( opts.fn ){ opts.fn(); }

    });
  }

  cy.nodes().forEach(function(n){
    var g = n.data('name');

    n.qtip({
      position: {
        my: 'top center',
        at: 'bottom center'
      },
      style: {
        classes: 'qtip-bootstrap',
        tip: {
          width: 16,
          height: 8
        }
      }
    });
  });

  $('#config-toggle').on('click', function(){
    $('body').toggleClass('config-closed');
    cy.resize();
  });
});

$(function() {
  FastClick.attach( document.body );
});
