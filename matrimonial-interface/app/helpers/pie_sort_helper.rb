module PieSortHelper
    def pieSort(c, f, l, k, y)

        if c == 1
            @profiles.sort_by!(&:cultureScore).reverse!
        elsif c == 2
            @profiles.sort_by!(&:facialScore).reverse!
        elsif c == 3
            @profiles.sort_by!(&:lifestyleScore).reverse!
        elsif c == 4
            @profiles.sort_by!(&:kundaliScore).reverse!
        elsif c == 5
            @profiles.sort_by!(&:locationScore).reverse!
        end
    end
end