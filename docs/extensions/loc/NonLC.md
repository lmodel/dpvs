---
search:
  boost: 10.0
---

# Class: NonLC 


_Set of jurisdictions that are not in LC_



<div data-search-exclude markdown="1">



URI: [loc:non-LC](https://w3id.org/lmodel/dpv/loc/non-LC)





```mermaid
 classDiagram
    class NonLC
    click NonLC href "../NonLC/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:non-LC](https://w3id.org/lmodel/dpv/loc/non-LC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* non-LC




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#non-LC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:non-LC |
| native | loc:NonLC |
| exact | dpv_loc:non-LC, dpv_loc_owl:non-LC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: nonLC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-LC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in LC
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-LC
exact_mappings:
- dpv_loc:non-LC
- dpv_loc_owl:non-LC
class_uri: loc:non-LC

```
</details>

### Induced

<details>
```yaml
name: nonLC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-LC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in LC
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-LC
exact_mappings:
- dpv_loc:non-LC
- dpv_loc_owl:non-LC
class_uri: loc:non-LC

```
</details></div>