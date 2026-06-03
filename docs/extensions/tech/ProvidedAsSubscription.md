---
search:
  boost: 10.0
---

# Class: ProvidedAsSubscription 


_Technology that is provided or used as a periodic subscription_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsSubscription](https://w3id.org/lmodel/dpv/tech/ProvidedAsSubscription)





```mermaid
 classDiagram
    class ProvidedAsSubscription
    click ProvidedAsSubscription href "../ProvidedAsSubscription/"
      ProvisionMethod <|-- ProvidedAsSubscription
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsSubscription**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsSubscription](https://w3id.org/lmodel/dpv/tech/ProvidedAsSubscription) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as SubscriptionProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsSubscription |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsSubscription |
| native | tech:ProvidedAsSubscription |
| exact | dpv_tech:ProvidedAsSubscription, dpv_tech_owl:ProvidedAsSubscription |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsSubscription
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSubscription
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology that is provided or used as a periodic subscription
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as SubscriptionProvision
exact_mappings:
- dpv_tech:ProvidedAsSubscription
- dpv_tech_owl:ProvidedAsSubscription
is_a: ProvisionMethod
class_uri: tech:ProvidedAsSubscription

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsSubscription
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSubscription
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology that is provided or used as a periodic subscription
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as SubscriptionProvision
exact_mappings:
- dpv_tech:ProvidedAsSubscription
- dpv_tech_owl:ProvidedAsSubscription
is_a: ProvisionMethod
class_uri: tech:ProvidedAsSubscription

```
</details></div>