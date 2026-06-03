---
search:
  boost: 10.0
---

# Class: PaymentCardExpiry 


_Information about payment card expiry such as a date_



<div data-search-exclude markdown="1">



URI: [pd:PaymentCardExpiry](https://w3id.org/lmodel/dpv/pd/PaymentCardExpiry)





```mermaid
 classDiagram
    class PaymentCardExpiry
    click PaymentCardExpiry href "../PaymentCardExpiry/"
      PaymentCard <|-- PaymentCardExpiry
        click PaymentCard href "../PaymentCard/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [FinancialAccount](FinancialAccount.md)
        * [PaymentCard](PaymentCard.md)
            * **PaymentCardExpiry**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PaymentCardExpiry](https://w3id.org/lmodel/dpv/pd/PaymentCardExpiry) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Payment Card Expiry




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PaymentCardExpiry |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PaymentCardExpiry |
| native | pd:PaymentCardExpiry |
| exact | dpv_pd:PaymentCardExpiry, dpv_pd_owl:PaymentCardExpiry |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PaymentCardExpiry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCardExpiry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card expiry such as a date
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card Expiry
exact_mappings:
- dpv_pd:PaymentCardExpiry
- dpv_pd_owl:PaymentCardExpiry
is_a: PaymentCard
class_uri: pd:PaymentCardExpiry

```
</details>

### Induced

<details>
```yaml
name: PaymentCardExpiry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PaymentCardExpiry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about payment card expiry such as a date
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Payment Card Expiry
exact_mappings:
- dpv_pd:PaymentCardExpiry
- dpv_pd_owl:PaymentCardExpiry
is_a: PaymentCard
class_uri: pd:PaymentCardExpiry

```
</details></div>