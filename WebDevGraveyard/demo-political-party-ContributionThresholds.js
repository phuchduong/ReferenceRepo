function getContributionRange(contribAmt) {
    // median campaign contribution 500
    var contribBin = "";
    if (contribAmt <= 300) { contribBin = "[200,300]"; }
    else if (contribAmt <= 500) { contribBin = "(300,500],"; }
    else if (contribAmt <= 1000) { contribBin = "(500,1e+03]"; }
    else if (contribAmt <= 1500) { contribBin = "(1e+03,1.5e+03]"; }
    else if (contribAmt <= 2000) { contribBin = "(1.5e+03,2e+03]"; }
    else if (contribAmt <= 2500) { contribBin = "(2e+03,2.5e+03]"; }
    else if (contribAmt <= 5000) { contribBin = "(2.5e+03,5e+03]"; }
    else if (contribAmt <= 10000) { contribBin = "(5e+03,1e+04]"; }
    else if (contribAmt <= 50000) { contribBin = "(1e+04,5e+04]"; }
    else if (contribAmt <= 10300000) { contribBin = "(5e+04,1.03e+07]"; }
    return contribBin;
};