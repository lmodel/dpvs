---
search:
  boost: 10.0
---

# Class: NonID 


_Set of jurisdictions that are not in ID_



<div data-search-exclude markdown="1">



URI: [loc:non-ID](https://w3id.org/lmodel/dpv/loc/non-ID)





```mermaid
 classDiagram
    class NonID
    click NonID href "../NonID/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:non-ID](https://w3id.org/lmodel/dpv/loc/non-ID) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* non-ID




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#non-ID |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:non-ID |
| native | loc:NonID |
| exact | dpv_loc:non-ID, dpv_loc_owl:non-ID |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: nonID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-ID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in ID
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-ID
exact_mappings:
- dpv_loc:non-ID
- dpv_loc_owl:non-ID
class_uri: loc:non-ID

```
</details>

### Induced

<details>
```yaml
name: nonID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-ID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in ID
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-ID
exact_mappings:
- dpv_loc:non-ID
- dpv_loc_owl:non-ID
class_uri: loc:non-ID

```
</details></div>