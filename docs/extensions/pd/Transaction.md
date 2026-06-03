---
search:
  boost: 10.0
---

# Class: Transaction 


_Information about financial transactions e.g. bank transfers_



<div data-search-exclude markdown="1">



URI: [pd:Transaction](https://w3id.org/lmodel/dpv/pd/Transaction)





```mermaid
 classDiagram
    class Transaction
    click Transaction href "../Transaction/"
      Transactional <|-- Transaction
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Transaction**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Transaction](https://w3id.org/lmodel/dpv/pd/Transaction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Transaction




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Transaction |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Transaction |
| native | pd:Transaction |
| exact | dpv_pd:Transaction, dpv_pd_owl:Transaction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Transaction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Transaction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial transactions e.g. bank transfers
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Transaction
exact_mappings:
- dpv_pd:Transaction
- dpv_pd_owl:Transaction
is_a: Transactional
class_uri: pd:Transaction

```
</details>

### Induced

<details>
```yaml
name: Transaction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Transaction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial transactions e.g. bank transfers
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Transaction
exact_mappings:
- dpv_pd:Transaction
- dpv_pd_owl:Transaction
is_a: Transactional
class_uri: pd:Transaction

```
</details></div>