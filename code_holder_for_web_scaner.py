"""
from candlestick_pattern import candlestick_patterns

# expander scan candle
with st.expander("Patterns Scaner"):

    # Select Crypto to find pattern button
    #select_crypto_name_scan = st.selectbox('Select Crypto to find pattern', crypto_names.crypto_name_tuple)

    # Select Patterns button
    patterns = st.selectbox('Select Patterns',candlestick_patterns)
    print(candlestick_patterns.get(patterns))

    # dict
    if st.button(f'Scan for {patterns}'):
        datafiles = os.listdir('dataset/daily')  # get lists of all CSV files

        #load_data_pattern(select_crypto_name_scan)

        import functions.plot_with_bokeh
        #functions.plot_with_bokeh.plot_candle_stick(select_crypto_name_scan)
        #st.bokeh_chart(functions.plot_with_bokeh.plot_candle_stick(select_crypto_name_scan), use_container_width=True)


        for filename in datafiles:  # loop for each file
            df = pd.read_csv(f'dataset/daily/{filename}')
            df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)


            pattern_function = getattr(talib, candlestick_patterns.get(patterns))
               # getattr talib.pattern / pattern = select option input from web
            symbol = filename.split('.')[0]  # get symbol from filename

            with open('dataset/crypto_list.csv') as f:
                for row in csv.reader(f):
                    crypto_dict[row[0]] = {'crypto': row[0].split('-')[0] + "-USD"}

            try:

                # result is the daily that returned after applied ta-lib candle pattern
                result = pattern_function(df['open'], df['high'], df['low'], df['close'])


                # last is the result lasttest value
                last = result.tail(1).values[0]


                if last == 100:
                    crypto_dict[symbol][candlestick_patterns.get(patterns)] = f'Bullish [Type Pattern'  # set pattern value to use
                    print(crypto_dict[symbol], "\n")
                    print(crypto_dict[symbol]['crypto'])
                    functions.plot_with_bokeh.plot_candle_stick(crypto_dict[symbol]['crypto'])
                    st.subheader(f"{symbol} {crypto_dict[symbol][candlestick_patterns.get(patterns)]}-{patterns}]")
                    st.bokeh_chart(functions.plot_with_bokeh.plot_candle_stick(crypto_dict[symbol]['crypto']))


                elif last == -100:
                    crypto_dict[symbol][candlestick_patterns.get(patterns)] = 'Bearish [Type Pattern'
                    print(crypto_dict[symbol], "\n")
                    functions.plot_with_bokeh.plot_candle_stick(crypto_dict[symbol]['crypto'])
                    st.subheader(f"{symbol} {crypto_dict[symbol][candlestick_patterns.get(patterns)]}-{patterns}]")
                    st.bokeh_chart(functions.plot_with_bokeh.plot_candle_stick(crypto_dict[symbol]['crypto']))



                else:
                    crypto_dict[symbol][patterns] = None



            except:
                pass
"""
