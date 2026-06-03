---
search:
  boost: 10.0
---

# Class: Income 


_Information about financial income e.g. for individual or household or_

_family_



<div data-search-exclude markdown="1">



URI: [pd:Income](https://w3id.org/lmodel/dpv/pd/Income)





```mermaid
 classDiagram
    class Income
    click Income href "../Income/"
      Transactional <|-- Income
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Income**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Income](https://w3id.org/lmodel/dpv/pd/Income) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Income




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Income |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Income |
| native | pd:Income |
| exact | dpv_pd:Income, dpv_pd_owl:Income |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Income
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Income
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about financial income e.g. for individual or household
  or

  family'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Income
exact_mappings:
- dpv_pd:Income
- dpv_pd_owl:Income
is_a: Transactional
class_uri: pd:Income

```
</details>

### Induced

<details>
```yaml
name: Income
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Income
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about financial income e.g. for individual or household
  or

  family'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Income
exact_mappings:
- dpv_pd:Income
- dpv_pd_owl:Income
is_a: Transactional
class_uri: pd:Income

```
</details></div>