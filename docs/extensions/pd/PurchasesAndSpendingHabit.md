---
search:
  boost: 10.0
---

# Class: PurchasesAndSpendingHabit 


_Information about analysis of purchases made and money spent expressed_

_as a habit e.g. monthly shopping trends_



<div data-search-exclude markdown="1">



URI: [pd:PurchasesAndSpendingHabit](https://w3id.org/lmodel/dpv/pd/PurchasesAndSpendingHabit)





```mermaid
 classDiagram
    class PurchasesAndSpendingHabit
    click PurchasesAndSpendingHabit href "../PurchasesAndSpendingHabit/"
      Transactional <|-- PurchasesAndSpendingHabit
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **PurchasesAndSpendingHabit**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PurchasesAndSpendingHabit](https://w3id.org/lmodel/dpv/pd/PurchasesAndSpendingHabit) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Purchases and Spending Habit




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PurchasesAndSpendingHabit |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PurchasesAndSpendingHabit |
| native | pd:PurchasesAndSpendingHabit |
| exact | dpv_pd:PurchasesAndSpendingHabit, dpv_pd_owl:PurchasesAndSpendingHabit |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PurchasesAndSpendingHabit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PurchasesAndSpendingHabit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about analysis of purchases made and money spent expressed

  as a habit e.g. monthly shopping trends'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Purchases and Spending Habit
exact_mappings:
- dpv_pd:PurchasesAndSpendingHabit
- dpv_pd_owl:PurchasesAndSpendingHabit
is_a: Transactional
class_uri: pd:PurchasesAndSpendingHabit

```
</details>

### Induced

<details>
```yaml
name: PurchasesAndSpendingHabit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PurchasesAndSpendingHabit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about analysis of purchases made and money spent expressed

  as a habit e.g. monthly shopping trends'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Purchases and Spending Habit
exact_mappings:
- dpv_pd:PurchasesAndSpendingHabit
- dpv_pd_owl:PurchasesAndSpendingHabit
is_a: Transactional
class_uri: pd:PurchasesAndSpendingHabit

```
</details></div>