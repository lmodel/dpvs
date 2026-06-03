---
search:
  boost: 10.0
---

# Class: NonFK 


_Set of jurisdictions that are not in FK_



<div data-search-exclude markdown="1">



URI: [loc:non-FK](https://w3id.org/lmodel/dpv/loc/non-FK)





```mermaid
 classDiagram
    class NonFK
    click NonFK href "../NonFK/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:non-FK](https://w3id.org/lmodel/dpv/loc/non-FK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* non-FK




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#non-FK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:non-FK |
| native | loc:NonFK |
| exact | dpv_loc:non-FK, dpv_loc_owl:non-FK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: nonFK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-FK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in FK
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-FK
exact_mappings:
- dpv_loc:non-FK
- dpv_loc_owl:non-FK
class_uri: loc:non-FK

```
</details>

### Induced

<details>
```yaml
name: nonFK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-FK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in FK
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-FK
exact_mappings:
- dpv_loc:non-FK
- dpv_loc_owl:non-FK
class_uri: loc:non-FK

```
</details></div>