---
search:
  boost: 10.0
---

# Class: Sale 


_Information about sales e.g. selling of goods or services_



<div data-search-exclude markdown="1">



URI: [pd:Sale](https://w3id.org/lmodel/dpv/pd/Sale)





```mermaid
 classDiagram
    class Sale
    click Sale href "../Sale/"
      Transactional <|-- Sale
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **Sale**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Sale](https://w3id.org/lmodel/dpv/pd/Sale) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Sale




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Sale |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Sale |
| native | pd:Sale |
| exact | dpv_pd:Sale, dpv_pd_owl:Sale |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sale
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sale
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sales e.g. selling of goods or services
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sale
exact_mappings:
- dpv_pd:Sale
- dpv_pd_owl:Sale
is_a: Transactional
class_uri: pd:Sale

```
</details>

### Induced

<details>
```yaml
name: Sale
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sale
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sales e.g. selling of goods or services
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sale
exact_mappings:
- dpv_pd:Sale
- dpv_pd_owl:Sale
is_a: Transactional
class_uri: pd:Sale

```
</details></div>