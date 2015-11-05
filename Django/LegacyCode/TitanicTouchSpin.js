    $("#ageInput").TouchSpin({
       buttondown_class: 'btn green',
       buttonup_class: 'btn green',
       min: 0,
       max: 80,
       stepinterval: 1,
       maxboostedstep: 5,
       postfix: 'years'
    });
    $("#SiblingSpouseSpin").TouchSpin({
        buttondown_class: 'btn green',
        buttonup_class: 'btn green',
        min: 0,
        max: 8,
        stepinterval: 1,
        maxboostedstep: 2
    });
    $("#parentChildSpin").TouchSpin({
        buttondown_class: 'btn green',
        buttonup_class: 'btn green',
        min: 0,
        max: 6,
        stepinterval: 1,
        maxboostedstep: 2
    });
    $("#fareSpin").TouchSpin({
        buttondown_class: 'btn green',
        buttonup_class: 'btn green',
        min: 0,
        max: 512,
        stepinterval: 1,
        maxboostedstep: 5,
        prefix: '$'
    });  