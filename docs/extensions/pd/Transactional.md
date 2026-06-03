---
search:
  boost: 10.0
---

# Class: Transactional 


_Information about a purchasing, spending or income_



<div data-search-exclude markdown="1">



URI: [pd:Transactional](https://w3id.org/lmodel/dpv/pd/Transactional)





```mermaid
 classDiagram
    class Transactional
    click Transactional href "../Transactional/"
      Financial <|-- Transactional
        click Financial href "../Financial/"
      

      Transactional <|-- Credit
        click Credit href "../Credit/"
      Transactional <|-- Income
        click Income href "../Income/"
      Transactional <|-- LoanRecord
        click LoanRecord href "../LoanRecord/"
      Transactional <|-- Purchase
        click Purchase href "../Purchase/"
      Transactional <|-- PurchasesAndSpendingHabit
        click PurchasesAndSpendingHabit href "../PurchasesAndSpendingHabit/"
      Transactional <|-- Sale
        click Sale href "../Sale/"
      Transactional <|-- Tax
        click Tax href "../Tax/"
      Transactional <|-- Transaction
        click Transaction href "../Transaction/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * **Transactional**
        * [Credit](Credit.md)
        * [Income](Income.md)
        * [LoanRecord](LoanRecord.md)
        * [Purchase](Purchase.md)
        * [PurchasesAndSpendingHabit](PurchasesAndSpendingHabit.md)
        * [Sale](Sale.md)
        * [Tax](Tax.md)
        * [Transaction](Transaction.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Transactional](https://w3id.org/lmodel/dpv/pd/Transactional) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Transactional




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Transactional |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Transactional |
| native | pd:Transactional |
| exact | dpv_pd:Transactional, dpv_pd_owl:Transactional |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Transactional
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Transactional
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about a purchasing, spending or income
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Transactional
exact_mappings:
- dpv_pd:Transactional
- dpv_pd_owl:Transactional
is_a: Financial
class_uri: pd:Transactional

```
</details>

### Induced

<details>
```yaml
name: Transactional
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Transactional
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about a purchasing, spending or income
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Transactional
exact_mappings:
- dpv_pd:Transactional
- dpv_pd_owl:Transactional
is_a: Financial
class_uri: pd:Transactional

```
</details></div>