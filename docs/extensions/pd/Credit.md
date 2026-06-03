---
search:
  boost: 10.0
---

# Class: Credit 


_Information about reputation with regards to money_



<div data-search-exclude markdown="1">



URI: [pd:Credit](https://w3id.org/lmodel/dpv/pd/Credit)





```mermaid
 classDiagram
    class Credit
    click Credit href "../Credit/"
      Transactional <|-- Credit
        click Transactional href "../Transactional/"
      

      Credit <|-- CreditCapacity
        click CreditCapacity href "../CreditCapacity/"
      Credit <|-- CreditRecord
        click CreditRecord href "../CreditRecord/"
      Credit <|-- CreditStanding
        click CreditStanding href "../CreditStanding/"
      Credit <|-- CreditWorthiness
        click CreditWorthiness href "../CreditWorthiness/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Credit**
            * [CreditCapacity](CreditCapacity.md)
            * [CreditRecord](CreditRecord.md)
            * [CreditStanding](CreditStanding.md)
            * [CreditWorthiness](CreditWorthiness.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Credit](https://w3id.org/lmodel/dpv/pd/Credit) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Credit |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Credit |
| native | pd:Credit |
| exact | dpv_pd:Credit, dpv_pd_owl:Credit |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Credit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Credit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about reputation with regards to money
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit
exact_mappings:
- dpv_pd:Credit
- dpv_pd_owl:Credit
is_a: Transactional
class_uri: pd:Credit

```
</details>

### Induced

<details>
```yaml
name: Credit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Credit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about reputation with regards to money
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit
exact_mappings:
- dpv_pd:Credit
- dpv_pd_owl:Credit
is_a: Transactional
class_uri: pd:Credit

```
</details></div>