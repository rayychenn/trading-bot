## Adjusted Stepgain algo

## Loop through each price for the backtesting

    ## Pull last X prices - specified in variables
    ## Calculate historic volatility over last Y periods
    ## Calculate current volatility of the pair
    ## Calculate the RSI to get a basic indication of overbought/underbought
        ## If overbought, set up negative step gain
            ## Use negative parameters (buy at -5, sell at +2)
            ## Do we want to use trends here?
        ## If oversold, set up positive step gain
            ## Use positive parameters (buy at -2, sell at +5) - have these as variables
            ## Tiering?? (i.e. x at -2, y at -4, z at -6) -> Use the volatility calculation to inform what this variable should be
                ## Apply a multiple??

        ## Return position and don't trade above amounts X + Y + Z


