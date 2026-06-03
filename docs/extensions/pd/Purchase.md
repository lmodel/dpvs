---
search:
  boost: 10.0
---

# Class: Purchase 


_Information about purchases such as items bought e.g. grocery or_

_clothing_



<div data-search-exclude markdown="1">



URI: [pd:Purchase](https://w3id.org/lmodel/dpv/pd/Purchase)





```mermaid
 classDiagram
    class Purchase
    click Purchase href "../Purchase/"
      Transactional <|-- Purchase
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Purchase**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Purchase](https://w3id.org/lmodel/dpv/pd/Purchase) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Purchase




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Purchase |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Purchase |
| native | pd:Purchase |
| exact | dpv_pd:Purchase, dpv_pd_owl:Purchase |
| related | svd:Purchase |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Purchase
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Purchase
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about purchases such as items bought e.g. grocery or

  clothing'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Purchase
exact_mappings:
- dpv_pd:Purchase
- dpv_pd_owl:Purchase
related_mappings:
- svd:Purchase
is_a: Transactional
class_uri: pd:Purchase

```
</details>

### Induced

<details>
```yaml
name: Purchase
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Purchase
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about purchases such as items bought e.g. grocery or

  clothing'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Purchase
exact_mappings:
- dpv_pd:Purchase
- dpv_pd_owl:Purchase
related_mappings:
- svd:Purchase
is_a: Transactional
class_uri: pd:Purchase

```
</details></div>