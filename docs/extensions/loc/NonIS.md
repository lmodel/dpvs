---
search:
  boost: 10.0
---

# Class: NonIS 


_Set of jurisdictions that are not in IS_



<div data-search-exclude markdown="1">



URI: [loc:non-IS](https://w3id.org/lmodel/dpv/loc/non-IS)





```mermaid
 classDiagram
    class NonIS
    click NonIS href "../NonIS/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:non-IS](https://w3id.org/lmodel/dpv/loc/non-IS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* non-IS




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#non-IS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:non-IS |
| native | loc:NonIS |
| exact | dpv_loc:non-IS, dpv_loc_owl:non-IS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: nonIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in IS
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-IS
exact_mappings:
- dpv_loc:non-IS
- dpv_loc_owl:non-IS
class_uri: loc:non-IS

```
</details>

### Induced

<details>
```yaml
name: nonIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in IS
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-IS
exact_mappings:
- dpv_loc:non-IS
- dpv_loc_owl:non-IS
class_uri: loc:non-IS

```
</details></div>