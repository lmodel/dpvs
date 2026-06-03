---
search:
  boost: 10.0
---

# Class: PaymentCardNumber 


_Information about payment card number_



<div data-search-exclude markdown="1">



URI: [pd:PaymentCardNumber](https://w3id.org/lmodel/dpv/pd/PaymentCardNumber)





```mermaid
 classDiagram
    class PaymentCardNumber
    click PaymentCardNumber href "../PaymentCardNumber/"
      PaymentCard <|-- PaymentCardNumber
        click PaymentCard href "../PaymentCard/"
      AccountIdentifier <|-- PaymentCardNumber
        click AccountIdentifier href "../AccountIdentifier/"
      

      PaymentCardNumber <|-- CreditCardNumber
        click CreditCardNumber href "../CreditCardNumber/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * [AccountIdentifier](AccountIdentifier.md)
            * **PaymentCardNumber** [ [PaymentCard](PaymentCard.md)]
                * [CreditCardNumber](CreditCardNumber.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PaymentCardNumber](https://w3id.org/lmodel/dpv/pd/PaymentCardNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Payment Card Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PaymentCardNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PaymentCardNumber |
| native | pd:PaymentCardNumber |
| exact | dpv_pd:PaymentCardNumber, dpv_pd_owl:PaymentCardNumber |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PaymentCardNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCardNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card Number
exact_mappings:
- dpv_pd:PaymentCardNumber
- dpv_pd_owl:PaymentCardNumber
is_a: AccountIdentifier
mixins:
- PaymentCard
class_uri: pd:PaymentCardNumber

```
</details>

### Induced

<details>
```yaml
name: PaymentCardNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCardNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card Number
exact_mappings:
- dpv_pd:PaymentCardNumber
- dpv_pd_owl:PaymentCardNumber
is_a: AccountIdentifier
mixins:
- PaymentCard
class_uri: pd:PaymentCardNumber

```
</details></div>