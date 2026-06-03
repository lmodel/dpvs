---
search:
  boost: 10.0
---

# Class: Tax 


_Information about financial tax e.g. tax records or tax due_



<div data-search-exclude markdown="1">



URI: [pd:Tax](https://w3id.org/lmodel/dpv/pd/Tax)





```mermaid
 classDiagram
    class Tax
    click Tax href "../Tax/"
      Transactional <|-- Tax
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Tax**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Tax](https://w3id.org/lmodel/dpv/pd/Tax) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Tax




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Tax |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Tax |
| native | pd:Tax |
| exact | dpv_pd:Tax, dpv_pd_owl:Tax |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tax
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tax
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial tax e.g. tax records or tax due
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tax
exact_mappings:
- dpv_pd:Tax
- dpv_pd_owl:Tax
is_a: Transactional
class_uri: pd:Tax

```
</details>

### Induced

<details>
```yaml
name: Tax
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tax
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial tax e.g. tax records or tax due
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tax
exact_mappings:
- dpv_pd:Tax
- dpv_pd_owl:Tax
is_a: Transactional
class_uri: pd:Tax

```
</details></div>