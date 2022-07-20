Feature: Checking if the element displayed in web are available and get the price

  Scenario: Check the price and if there are stock from URL given
    Given I navigate to "https://www.decathlon.es/es/p/kit-de-pesas-y-barras-de-musculacion-de-50-kg/_/R-p-335265?mc=8655649&_adin=11551547647" URL for "DecathPesasMancuernas" web page
    And I wait for page "DecathPesasMancuernas" completely loaded
    Then the item is available to purchase
    And the price is "149,99 €"