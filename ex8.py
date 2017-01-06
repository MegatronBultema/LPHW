formatter ="%s %s %s %s"

print formatter %(1,2,3,4)
print formatter %('one', 'two', 'three', 'four')
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "I had this thing.",
    "that you could type right.",
    "but it didn't sing.",
    "So I siad goodnight."
    )

