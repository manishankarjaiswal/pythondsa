def regroup_book(book, max_cap):
    book_op = [] # Stores the regrouped chapters
    remaining_book = book[:] # Creates a copy of the original book to avoid modifying it

    while remaining_book: # Loop until all chapters have been processed
        count = 0 # Tracks the total number of questions in the current chapter
        chapter = []  # Stores the current chapter being formed
        new_remaining_book = [] # Stores chapters that couldn't be added to the current chapter

        for ind in range(len(remaining_book)):
            extra_count = sum(remaining_book[ind]) # Calculates the total questions in the current chapter
            if count + extra_count < max_cap+1: # If adding the chapter doesn't exceed the limit
                count += extra_count
                chapter.extend(remaining_book[ind]) # Add the chapter to the current chapter
            else:
                new_remaining_book.append(remaining_book[ind]) # Add the chapter to the remaining book

        # If chapter exist
        if chapter:
            book_op.append(chapter) # Add the completed chapter to the output
            remaining_book = new_remaining_book # Update the remaining book
        else:
            # If no chapters fit, add the remaining items directly to the output
            book_op.extend(remaining_book)
            break

    return book_op

book = [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [40], [1, 2], [1, 3, 2], [48]]
max_cap = 30
print(regroup_book(book, max_cap))