---
search:
  boost: 10.0
---

# Class: CreditCardNumber 


_Information about credit card number_



<div data-search-exclude markdown="1">



URI: [pd:CreditCardNumber](https://w3id.org/lmodel/dpv/pd/CreditCardNumber)





```mermaid
 classDiagram
    class CreditCardNumber
    click CreditCardNumber href "../CreditCardNumber/"
      PaymentCardNumber <|-- CreditCardNumber
        click PaymentCardNumber href "../PaymentCardNumber/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * [AccountIdentifier](AccountIdentifier.md)
            * [PaymentCardNumber](PaymentCardNumber.md) [ [PaymentCard](PaymentCard.md)]
                * **CreditCardNumber**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditCardNumber](https://w3id.org/lmodel/dpv/pd/CreditCardNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Card Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditCardNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditCardNumber |
| native | pd:CreditCardNumber |
| exact | dpv_pd:CreditCardNumber, dpv_pd_owl:CreditCardNumber |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditCardNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditCardNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit card number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Card Number
exact_mappings:
- dpv_pd:CreditCardNumber
- dpv_pd_owl:CreditCardNumber
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: PaymentCardNumber
class_uri: pd:CreditCardNumber

```
</details>

### Induced

<details>
```yaml
name: CreditCardNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditCardNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit card number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Card Number
exact_mappings:
- dpv_pd:CreditCardNumber
- dpv_pd_owl:CreditCardNumber
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: PaymentCardNumber
class_uri: pd:CreditCardNumber

```
</details></div>