---
search:
  boost: 10.0
---

# Class: Financial 


_Information about finance including monetary characteristics and_

_transactions_



<div data-search-exclude markdown="1">



URI: [pd:Financial](https://w3id.org/lmodel/dpv/pd/Financial)





```mermaid
 classDiagram
    class Financial
    click Financial href "../Financial/"
      Financial <|-- FinancialAccount
        click FinancialAccount href "../FinancialAccount/"
      Financial <|-- FinancialStatus
        click FinancialStatus href "../FinancialStatus/"
      Financial <|-- Insurance
        click Insurance href "../Insurance/"
      Financial <|-- Ownership
        click Ownership href "../Ownership/"
      Financial <|-- Transactional
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* **Financial**
    * [FinancialAccount](FinancialAccount.md)
    * [FinancialStatus](FinancialStatus.md)
    * [Insurance](Insurance.md)
    * [Ownership](Ownership.md)
    * [Transactional](Transactional.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Financial](https://w3id.org/lmodel/dpv/pd/Financial) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Financial




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Financial |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Financial |
| native | pd:Financial |
| exact | dpv_pd:Financial, dpv_pd_owl:Financial |
| related | svd:Financial |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Financial
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Financial
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about finance including monetary characteristics and

  transactions'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial
exact_mappings:
- dpv_pd:Financial
- dpv_pd_owl:Financial
related_mappings:
- svd:Financial
class_uri: pd:Financial

```
</details>

### Induced

<details>
```yaml
name: Financial
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Financial
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about finance including monetary characteristics and

  transactions'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial
exact_mappings:
- dpv_pd:Financial
- dpv_pd_owl:Financial
related_mappings:
- svd:Financial
class_uri: pd:Financial

```
</details></div>