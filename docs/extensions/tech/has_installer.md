---
search:
  boost: 5.0
---

# Slot: has_installer 


_Indicates technology installer_



<div data-search-exclude markdown="1">



URI: [tech:has_installer](https://w3id.org/lmodel/dpv/tech/has_installer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_installer**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* has installer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasInstaller |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_installer |
| native | tech:has_installer |
| exact | dpv_tech:hasInstaller, dpv_tech_owl:hasInstaller |




## LinkML Source

<details>
```yaml
name: has_installer
definition_uri: tech:hasInstaller
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasInstaller
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology installer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has installer
exact_mappings:
- dpv_tech:hasInstaller
- dpv_tech_owl:hasInstaller
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>