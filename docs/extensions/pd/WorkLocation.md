---
search:
  boost: 10.0
---

# Class: WorkLocation 


_Information about a person's work place, including their location,_

_address, and locality_



<div data-search-exclude markdown="1">



URI: [pd:WorkLocation](https://w3id.org/lmodel/dpv/pd/WorkLocation)





```mermaid
 classDiagram
    class WorkLocation
    click WorkLocation href "../WorkLocation/"
      DpvLocation <|-- WorkLocation
        click DpvLocation href "../DpvLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **WorkLocation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:WorkLocation](https://w3id.org/lmodel/dpv/pd/WorkLocation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Work Place




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#WorkLocation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:WorkLocation |
| native | pd:WorkLocation |
| exact | dpv_pd:WorkLocation, dpv_pd_owl:WorkLocation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s work place, including their location,

  address, and locality'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work Place
exact_mappings:
- dpv_pd:WorkLocation
- dpv_pd_owl:WorkLocation
is_a: DpvLocation
class_uri: pd:WorkLocation

```
</details>

### Induced

<details>
```yaml
name: WorkLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s work place, including their location,

  address, and locality'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work Place
exact_mappings:
- dpv_pd:WorkLocation
- dpv_pd_owl:WorkLocation
is_a: DpvLocation
class_uri: pd:WorkLocation

```
</details></div>