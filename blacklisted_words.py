blacklisted_phrases=["pornography", "world war i", "machine gun", "hell", "fuck"];

phrases= ["the machine gun is hostile",
          "world war is aviodable",
          "the pornography industy is growing",
          "who  the hell",
          "he is a fucking piece of shit"]

def filter_blacklist(input):
  for black_word in blacklisted_phrases:
    #this was the only line left, we needed to add space 
    #(basically padding the word with spaces to make them 
    #distict words)
    padded_word= " "+ black_word +" "
    if input.endswith(black_word):
        print("unsafe") 
        break
    if padded_word in input:
        print("unsafe")
        break   
  else:
    print("safe")

filter_blacklist("the machine gun is hostile")
filter_blacklist("world war is aviodable")
filter_blacklist("the pornography industy is growing")
filter_blacklist("who the hell")
filter_blacklist("he is a fucking piece of shit")
