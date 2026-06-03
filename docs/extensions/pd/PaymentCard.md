---
search:
  boost: 10.0
---

# Class: PaymentCard 


_Information about payment card such as credit and debit cards_



<div data-search-exclude markdown="1">



URI: [pd:PaymentCard](https://w3id.org/lmodel/dpv/pd/PaymentCard)





```mermaid
 classDiagram
    class PaymentCard
    click PaymentCard href "../PaymentCard/"
      FinancialAccount <|-- PaymentCard
        click FinancialAccount href "../FinancialAccount/"
      

      PaymentCard <|-- PaymentCardExpiry
        click PaymentCardExpiry href "../PaymentCardExpiry/"
      PaymentCard <|-- PaymentCardNumber
        click PaymentCardNumber href "../PaymentCardNumber/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * **PaymentCard**
            * [PaymentCardExpiry](PaymentCardExpiry.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PaymentCard](https://w3id.org/lmodel/dpv/pd/PaymentCard) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Payment Card




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PaymentCard |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PaymentCard |
| native | pd:PaymentCard |
| exact | dpv_pd:PaymentCard, dpv_pd_owl:PaymentCard |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PaymentCard
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCard
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card such as credit and debit cards
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card
exact_mappings:
- dpv_pd:PaymentCard
- dpv_pd_owl:PaymentCard
is_a: FinancialAccount
class_uri: pd:PaymentCard

```
</details>

### Induced

<details>
```yaml
name: PaymentCard
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCard
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card such as credit and debit cards
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card
exact_mappings:
- dpv_pd:PaymentCard
- dpv_pd_owl:PaymentCard
is_a: FinancialAccount
class_uri: pd:PaymentCard

```
</details></div>